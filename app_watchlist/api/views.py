from app_watchlist.api.serializers import MovieSerializers
from app_watchlist.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET',))
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializers(movies, many=True)
    return Response(serializers.data)

@api_view(('GET',))
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializers = MovieSerializers(movie)
    return Response(serializers.data)