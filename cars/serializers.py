from rest_framework import serializers
from .models import Car, CarPhoto, PriceTier, Discount, AdditionalService


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['id', 'image', 'order']


class PriceTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTier
        fields = ['id', 'season', 'min_days', 'max_days', 'price_per_day']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'percent', 'start_date', 'end_date']


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ['id', 'name', 'price', 'is_active']


class CarSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)
    price_tiers = PriceTierSerializer(many=True, read_only=True)
    discounts = DiscountSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'body_type', 'color', 'drive_type',
            'engine_power', 'seats', 'year', 'deposit_amount',
            'description', 'is_active', 'photos', 'price_tiers', 'discounts',
        ]