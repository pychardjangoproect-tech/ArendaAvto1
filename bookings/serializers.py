from rest_framework import serializers
from datetime import date
from cars.models import PriceTier, Discount
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'car', 'full_name', 'phone', 'start_date', 'end_date',
            'pickup_time', 'delivery_point', 'additional_services',
            'total_price', 'status', 'agreed_to_terms', 'created_at',
        ]
        read_only_fields = ['total_price', 'status', 'created_at']

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError('Дата окончания должна быть позже даты начала.')
        return data

    def create(self, validated_data):
        services = validated_data.pop('additional_services', [])
        car = validated_data['car']
        start = validated_data['start_date']
        end = validated_data['end_date']
        days = (end - start).days

        month = start.month
        season = 'summer' if 4 <= month <= 9 else 'winter'

        price_tiers = PriceTier.objects.filter(car=car, season=season, min_days__lte=days)
        tier = None
        for t in price_tiers:
            if t.max_days is None or days <= t.max_days:
                tier = t
                break

        if not tier:
            raise serializers.ValidationError('Для этого срока аренды не найден тариф.')

        price = tier.price_per_day * days

        discount = Discount.objects.filter(
            car=car, start_date__lte=start, end_date__gte=start
        ).first()
        if discount:
            price = price * (100 - discount.percent) / 100

        services_total = sum(s.price for s in services)
        total = price + services_total

        booking = Booking.objects.create(total_price=total, **validated_data)
        booking.additional_services.set(services)
        return booking