from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'source', 'rating', 'date')
    list_filter = ('source', 'rating')