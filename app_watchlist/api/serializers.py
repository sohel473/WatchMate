from rest_framework import serializers
from app_watchlist.models import WatchList, StreamPlatform


class WatchListSerializers(serializers.ModelSerializer):

    # platform = serializers.ReadOnlyField(source='platform.name')

    class Meta:
        model = WatchList
        # fields = ('id', 'title', 'storyline', 'platform', 'active')
        fields = "__all__"
        # exclude = ['active']

    def to_representation(self, instance):
        rep = super(WatchListSerializers, self).to_representation(instance)
        rep['platform'] = instance.platform.name
        return rep


class StreamPlatformSerializers(serializers.ModelSerializer):

    watchlist = WatchListSerializers(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        # fields = ('id', 'name', 'about', 'website', 'watchlist')
        # exclude = ['active']
