from django.contrib import admin
from app_watchlist.models import WatchList, StreamPlatform

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
