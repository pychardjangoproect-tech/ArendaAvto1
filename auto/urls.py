from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from cars.views import home_view, catalog_view, car_detail_view
from attractions.views import route_list_view, route_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('catalog/', catalog_view, name='catalog'),
    path('car/<int:pk>/', car_detail_view, name='car_detail'),
    path('routes/', route_list_view, name='route_list'),
    path('routes/<int:pk>/', route_detail_view, name='route_detail'),

    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('api/', include('bookings.urls')),
    path('api/', include('attractions.urls')),
    path('api/', include('reviews.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)