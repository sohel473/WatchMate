from django.urls import path, include
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import ReviewDetail, ReviewList, StreanViewSet, WatchListAV, WatchListDetailsAV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'streams', StreanViewSet, basename='streams')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='movie-details'),

    #     path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    #     path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(),
    #          name='streamplatform-detail'),

    path('', include(router.urls)),


    #     path('review/', ReviewList.as_view(),
    #          name='review-detail'),
    #     path('review/<int:pk>/', ReviewDetail.as_view(),
    #          name='review-detail'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-detail'),
    path('<int:pk1>/review/<int:pk>/',
         ReviewDetail.as_view(), name='review-detail'),
]
