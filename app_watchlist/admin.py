from django.contrib import admin
from app_watchlist.models import Review, WatchList, StreamPlatform

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
