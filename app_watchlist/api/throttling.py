from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class WatchList_UserRateThrottle(UserRateThrottle):
    scope = 'watch-list-user'


class ReviewList_UserRateThrottle(UserRateThrottle):
    scope = 'review-list-user'


class WatchList_AnonRateThrottle(AnonRateThrottle):
    scope = 'watch-list-anon'


class ReviewList_AnonRateThrottle(AnonRateThrottle):
    scope = 'review-list-anon'
