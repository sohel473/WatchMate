from app_watchlist.api.serializers import WatchListSerializers, StreamPlatformSerializers
from app_watchlist.models import WatchList, StreamPlatform
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class StreamPlatformAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializers = StreamPlatformSerializers(
            platforms, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = StreamPlatformSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


class StreamPlatformDetailsAV(APIView):
    # def get_object(self, pk):
    #     try:
    #         return StreamPlatform.objects.get(pk=pk)
    #     except StreamPlatform.DoesNotExist:
    #         return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializers = StreamPlatformSerializers(platform)
        return Response(serializers.data)

    def put(self, request, pk):
        platform = self.get_object(pk)
        serializers = StreamPlatformSerializers(platform, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = self.get_object(pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

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
