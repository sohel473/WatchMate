from ast import Try
from app_watchlist.api.serializers import MovieSerializers
from app_watchlist.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(('GET', "POST"))
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializers = MovieSerializers(movies, many=True)
        return Response(serializers.data)
    if request.method == "POST":
        serializers = MovieSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

@api_view(('GET', 'PUT', 'DELETE'))
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializers = MovieSerializers(movie)
        return Response(serializers.data)
    if request.method == 'PUT':
        serializers = MovieSerializers(movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
