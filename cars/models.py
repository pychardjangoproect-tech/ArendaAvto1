from django.db import models


class Car(models.Model):
    class BodyType(models.TextChoices):
        SEDAN = 'sedan', 'Седан'
        SUV = 'suv', 'Внедорожник'
        MINIVAN = 'minivan', 'Минивэн'
        HATCHBACK = 'hatchback', 'Хэтчбек'
        UNIVERSAL = 'universal', 'Универсал'

    class DriveType(models.TextChoices):
        FRONT = 'front', 'Передний'
        REAR = 'rear', 'Задний'
        ALL = 'all', 'Полный'

    brand = models.CharField('Марка', max_length=100)
    model = models.CharField('Модель', max_length=100)
    body_type = models.CharField('Кузов', max_length=20, choices=BodyType.choices)
    color = models.CharField('Цвет', max_length=50)
    drive_type = models.CharField('Привод', max_length=10, choices=DriveType.choices)
    engine_power = models.CharField('Двигатель', max_length=50)
    seats = models.PositiveSmallIntegerField('Пассажирские места')
    year = models.PositiveSmallIntegerField('Год выпуска')
    deposit_amount = models.DecimalField('Залог', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', blank=True)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos', verbose_name='Машина')
    image = models.ImageField('Фото', upload_to='cars/')
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Фото машины'
        verbose_name_plural = 'Фото машин'
        ordering = ['order']


class PriceTier(models.Model):
    class Season(models.TextChoices):
        SUMMER = 'summer', 'Апрель — Сентябрь'
        WINTER = 'winter', 'Сентябрь — Март'

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='price_tiers', verbose_name='Машина')
    season = models.CharField('Сезон', max_length=10, choices=Season.choices)
    min_days = models.PositiveSmallIntegerField('Мин. дней')
    max_days = models.PositiveSmallIntegerField('Макс. дней', null=True, blank=True)
    price_per_day = models.DecimalField('Цена за сутки', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Прайс-лист'
        ordering = ['season', 'min_days']

    def __str__(self):
        return f'{self.car} [{self.get_season_display()}] {self.min_days}-{self.max_days or "∞"} дн.'


class Discount(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='discounts', verbose_name='Машина')
    percent = models.PositiveSmallIntegerField('Процент скидки')
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.car} -{self.percent}% ({self.start_date}—{self.end_date})'


class AdditionalService(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Доп. услуга'
        verbose_name_plural = 'Доп. услуги'

    def __str__(self):
        return self.name