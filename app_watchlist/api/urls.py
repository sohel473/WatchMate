from django.urls import path, include
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import ReviewDetail, ReviewList, StreamViewSet, WatchListAV, WatchListDetailsAV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'watch/streams', StreamViewSet, basename='streams')

urlpatterns = [
    path('watch/list/', WatchListAV.as_view(), name='movie-list'),
    path('watch/<int:pk>/', WatchListDetailsAV.as_view(), name='movie-details'),

    #     path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    #     path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(),
    #          name='streamplatform-detail'),s

    path('', include(router.urls)),


    #     path('review/', ReviewList.as_view(),
    #          name='review-detail'),
    #     path('review/<int:pk>/', ReviewDetail.as_view(),
    #          name='review-detail'),
    path('watch/<int:pk>/reviews/', ReviewList.as_view(), name='reviews'),
    path('watch/<int:pk1>/reviews/<int:pk>/',
         ReviewDetail.as_view(), name='review-detail'),
]
