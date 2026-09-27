from rest_framework import viewsets, permissions
from .models import Route
from .serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




from django.shortcuts import render, get_object_or_404
from .models import Route


def route_list_view(request):
    routes = Route.objects.all()
    return render(request, 'attractions/route_list.html', {'routes': routes})


def route_detail_view(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'attractions/route_detail.html', {'route': route})