from django.db import models
from cars.models import Car, AdditionalService


class Booking(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        CONFIRMED = 'confirmed', 'Подтверждена'
        CANCELLED = 'cancelled', 'Отменена'
        COMPLETED = 'completed', 'Завершена'

    class DeliveryPoint(models.TextChoices):
        CITY = 'city', 'Город'
        AIRPORT = 'airport', 'Аэропорт'

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    pickup_time = models.TimeField(null=True, blank=True)
    delivery_point = models.CharField(max_length=10, choices=DeliveryPoint.choices, default=DeliveryPoint.CITY)
    additional_services = models.ManyToManyField(AdditionalService, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)
    agreed_to_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} — {self.car} ({self.start_date}—{self.end_date})'