from django.contrib import admin
from .models import *

class RoutePhotoInline(admin.TabularInline):
    model = RoutePhoto
    extra = 1


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'distance_km')
    filter_horizontal = ('suggested_cars',)
    inlines = [RoutePhotoInline]