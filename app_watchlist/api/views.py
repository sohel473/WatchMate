from django.http import HttpResponse
from app_watchlist.api.serializers import MovieSerializers
from app_watchlist.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
    movie = Movie.objects.get(pk=pk)
    if request.method == 'GET':
        serializers = MovieSerializers(movie)
        return Response(serializers.data)
    if request.method == 'PUT':
        serializers = MovieSerializers(movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    if request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
