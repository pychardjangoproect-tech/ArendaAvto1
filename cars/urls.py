from rest_framework.routers import DefaultRouter
from .views import CarViewSet, AdditionalServiceViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)
router.register('services', AdditionalServiceViewSet)

urlpatterns = router.urls