from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from .models import Car, AdditionalService
from .serializers import CarSerializer, AdditionalServiceSerializer
from attractions.models import Route
from reviews.models import Review


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['body_type', 'drive_type', 'color', 'seats', 'year']
    ordering_fields = ['year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdditionalServiceViewSet(viewsets.ModelViewSet):
    queryset = AdditionalService.objects.filter(is_active=True)
    serializer_class = AdditionalServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def home_view(request):
    cars = Car.objects.filter(is_active=True)[:6]
    routes = Route.objects.all()[:3]
    reviews = Review.objects.all().order_by('-date')[:3]
    return render(request, 'cars/home.html', {'cars': cars, 'routes': routes, 'reviews': reviews})


def catalog_view(request):
    cars = Car.objects.filter(is_active=True)

    color = request.GET.get('color')
    drive_type = request.GET.get('drive_type')
    body_type = request.GET.get('body_type')
    seats = request.GET.get('seats')
    year = request.GET.get('year')
    sort = request.GET.get('sort', 'expensive')

    if color:
        cars = cars.filter(color=color)
    if drive_type:
        cars = cars.filter(drive_type=drive_type)
    if body_type:
        cars = cars.filter(body_type=body_type)
    if seats:
        cars = cars.filter(seats=seats)
    if year:
        cars = cars.filter(year=year)

    if sort == 'cheap':
        cars = sorted(cars, key=lambda c: c.price_tiers.first().price_per_day if c.price_tiers.first() else 0)
    elif sort == 'discount':
        cars = cars.filter(discounts__isnull=False).distinct()
    else:
        cars = sorted(cars, key=lambda c: c.price_tiers.first().price_per_day if c.price_tiers.first() else 0, reverse=True)

    context = {
        'cars': cars,
        'colors': Car.objects.values_list('color', flat=True).distinct(),
        'body_types': Car.BodyType.choices,
        'drive_types': Car.DriveType.choices,
        'years': Car.objects.values_list('year', flat=True).distinct().order_by('-year'),
        'current_sort': sort,
        'selected': {
            'color': color, 'drive_type': drive_type, 'body_type': body_type,
            'seats': seats, 'year': year,
        },
    }
    return render(request, 'cars/catalog.html', context)


def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    similar_cars = Car.objects.filter(is_active=True).exclude(pk=pk)[:3]
    return render(request, 'cars/car_detail.html', {'car': car, 'similar_cars': similar_cars})