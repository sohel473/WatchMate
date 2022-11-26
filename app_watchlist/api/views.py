from app_watchlist.api.pagination import WatchListLOPagination, WatchListPagination
from app_watchlist.api.serializers import AllReviewSerializer, WatchListSerializers, StreamPlatformSerializers, ReviewSerializer
from app_watchlist.models import WatchList, StreamPlatform, Review
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, mixins, generics, viewsets, filters
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from app_watchlist.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from app_watchlist.api.throttling import WatchList_UserRateThrottle, ReviewList_UserRateThrottle, WatchList_AnonRateThrottle, ReviewList_AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


class WatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializers
    pagination_class = WatchListLOPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['platform__name', 'active']
    search_fields = ['title', 'storyline']
    ordering_fields = ['avg_rating', 'created']


class AllReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = AllReviewSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['review_user', 'active']
    search_fields = ['watchlist__title', 'description']
    ordering_fields = ['watchlist__title', 'rating']

    # def get_queryset(self):
    #     reviews = Review.objects.all()
    #     # filter by user id
    #     # user_id = self.request.query_params.get('user')
    #     # or c
    #     user = self.request.query_params.get('user')
    #     print(user)
    #     # if user_id is not None:
    #     #     reviews = reviews.filter(review_user=user_id)
    #     if user is not None:
    #         reviews = reviews.filter(review_user__username=user)

    #     return reviews


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewList_UserRateThrottle,
    #                     WatchList_AnonRateThrottle]

    def get_queryset(self):
        # print(self.kwargs)
        watch_pk = self.kwargs['pk']
        reviews = Review.objects.filter(watchlist=watch_pk)
        isActive = self.request.query_params.get('isActive')
        print(isActive)
        if isActive is not None:
            reviews = Review.objects.filter(
                watchlist=watch_pk, active=isActive)
        return reviews

    def perform_create(self, serializer):
        watch_list = WatchList.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        review_exist = Review.objects.filter(
            watchlist=watch_list, review_user=user)

        if review_exist:
            raise ValidationError("You already reviewed this!")

        if watch_list.number_rating == 0:
            # print("nnum of rating = 0")
            watch_list.sum_rating = serializer.validated_data['rating']
            watch_list.avg_rating = serializer.validated_data['rating']
            watch_list.number_rating = 1
        else:
            # print("nnum of rating more than 0")
            watch_list.sum_rating += serializer.validated_data['rating']
            watch_list.number_rating += 1
            watch_list.avg_rating = watch_list.sum_rating / watch_list.number_rating
            # print(watch_list.sum_rating)
            # print(watch_list.number_rating)
            # print(watch_list.avg_rating)

        watch_list.save()

        serializer.save(watchlist=watch_list, review_user=user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]

    # def get_queryset(self):
    #     print(self.kwargs)
    #     review_pk = self.kwargs['pk']
    #     review = Review.objects.get(pk=review_pk)
    #     # print(review)
    #     return review


# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class StreamViewSet(viewsets.ModelViewSet):
    serializer_class = StreamPlatformSerializers
    queryset = StreamPlatform.objects.all()
    permission_classes = [IsAdminOrReadOnly]


# class StreamViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializers(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         stream = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializers(stream)
#         return Response(serializer.data)

#     def create(self, request):
#         serializers = StreamPlatformSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)

#     def update(self, request, pk=None):
#         platform = StreamPlatform.objects.get(pk=pk)
#         serializers = StreamPlatformSerializers(platform, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)

#     def destroy(self, request, pk=None):
#         platform = StreamPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class StreamPlatformAV(APIView):

#     def get(self, request):
#         platforms = StreamPlatform.objects.all()
#         serializers = StreamPlatformSerializers(
#             platforms, many=True)
#         return Response(serializers.data)

#     def post(self, request):
#         serializers = StreamPlatformSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)


# class StreamPlatformDetailsAV(APIView):
#     # def get_object(self, pk):
#     #     try:
#     #         return StreamPlatform.objects.get(pk=pk)
#     #     except StreamPlatform.DoesNotExist:
#     #         return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializers = StreamPlatformSerializers(platform)
#         return Response(serializers.data)

#     def put(self, request, pk):
#         platform = self.get_object(pk)
#         serializers = StreamPlatformSerializers(platform, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         platform = self.get_object(pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [WatchList_UserRateThrottle,
    #                     ReviewList_AnonRateThrottle]

    def get(self, request):
        movies = WatchList.objects.all()
        serializers = WatchListSerializers(movies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = WatchListSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


class WatchListDetailsAV(APIView):
    # def get_object(self, pk):
    #     try:
    #         return WatchList.objects.get(pk=pk)
    #     except WatchList.DoesNotExist:
    #         return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    permission_classes = [IsAuthenticated]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'watchlist-details'

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializers = WatchListSerializers(movie)
        return Response(serializers.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializers = WatchListSerializers(movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(('GET', "POST"))
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializers = MovieSerializers(movies, many=True)
#         return Response(serializers.data)
#     if request.method == "POST":
#         serializers = MovieSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)

# @api_view(('GET', 'PUT', 'DELETE'))
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializers = MovieSerializers(movie)
#         return Response(serializers.data)
#     if request.method == 'PUT':
#         serializers = MovieSerializers(movie, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
