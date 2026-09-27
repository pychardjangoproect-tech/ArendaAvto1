from rest_framework import serializers
from cars.serializers import CarSerializer
from .models import Route, RoutePhoto


class RoutePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutePhoto
        fields = ['id', 'image', 'order']


class RouteSerializer(serializers.ModelSerializer):
    photos = RoutePhotoSerializer(many=True, read_only=True)
    suggested_cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'title', 'duration', 'distance_km', 'description', 'cover_image', 'photos', 'suggested_cars']