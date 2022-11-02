from django.urls import path
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import ReviewDetail, ReviewList, WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='movie-details'),

    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(),
         name='streamplatform-detail'),

    #     path('review/', ReviewList.as_view(),
    #          name='review-detail'),
    #     path('review/<int:pk>/', ReviewDetail.as_view(),
    #          name='review-detail'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-detail'),
    path('<int:pk1>/review/<int:pk>/',
         ReviewDetail.as_view(), name='review-detail'),
]
