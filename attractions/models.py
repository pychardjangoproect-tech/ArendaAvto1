from django.db import models
from cars.models import Car


class Route(models.Model):
    title = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    distance_km = models.PositiveIntegerField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to='routes/')
    suggested_cars = models.ManyToManyField(Car, blank=True, related_name='suggested_for_routes')

    def __str__(self):
        return self.title


class RoutePhoto(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='routes/gallery/')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']