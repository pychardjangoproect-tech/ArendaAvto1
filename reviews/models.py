from django.db import models


class Review(models.Model):
    class Source(models.TextChoices):
        TWOGIS = '2gis', '2ГИС'
        YANDEX = 'yandex', 'Яндекс Карты'
        GOOGLE = 'google', 'Google Maps'

    source = models.CharField(max_length=10, choices=Source.choices)
    author_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='reviews/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.author_name} ({self.get_source_display()}, {self.rating}★)'