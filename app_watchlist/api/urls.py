from django.urls import path
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import MovieListAV, MovieListDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieListDetailsAV.as_view(), name='movie-details'),
]
