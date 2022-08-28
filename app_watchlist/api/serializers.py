from dataclasses import field, fields
from pyexpat import model
from wsgiref.validate import validator
from rest_framework import serializers
from app_watchlist.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # exclude = ['active']

    name_len = serializers.SerializerMethodField()

    def get_name_len(self, obj):
        return len(obj.name)

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Movies name and description are identical")
        return data

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")


# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     return value

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Movies name and description are identical")
#         return data
