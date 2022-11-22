from rest_framework import serializers
from app_watchlist.models import Review, WatchList, StreamPlatform


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class ReviewUserSerializer(serializers.ModelSerializer):
    # shows user name and watchlist name with read_only
    review_user = serializers.StringRelatedField()
    watchlist = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    # shows user name and watchlist name with write and update operations as well
    # def to_representation(self, instance):
    #     rep = super(ReviewUserSerializer, self).to_representation(instance)
    #     rep['review_user'] = instance.review_user.username
    #     rep['watchlist'] = instance.watchlist.title
    #     return rep


class WatchListSerializers(serializers.ModelSerializer):

    # platform = serializers.ReadOnlyField(source='platform.name')
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        # fields = ('id', 'title', 'storyline', 'platform', 'active')
        fields = "__all__"
        # exclude = ['active']

    # def to_representation(self, instance):
    #     rep = super(WatchListSerializers, self).to_representation(instance)
    #     rep['platform'] = instance.platform.name
    #     return rep


class StreamPlatformSerializers(serializers.ModelSerializer):

    watchlist = WatchListSerializers(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        # fields = ('id', 'name', 'about', 'website', 'watchlist')
        # exclude = ['active']
