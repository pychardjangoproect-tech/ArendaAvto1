from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'car', 'start_date', 'end_date', 'status', 'total_price')
    list_filter = ('status', 'delivery_point')
    search_fields = ('full_name', 'phone')