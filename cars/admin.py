from django.contrib import admin
from .models import Car, CarPhoto, PriceTier, Discount, AdditionalService


class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1


class PriceTierInline(admin.TabularInline):
    model = PriceTier
    extra = 1


class DiscountInline(admin.TabularInline):
    model = Discount
    extra = 0


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'body_type', 'year', 'is_active')
    list_filter = ('body_type', 'drive_type', 'is_active')
    inlines = [CarPhotoInline, PriceTierInline, DiscountInline]


@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')