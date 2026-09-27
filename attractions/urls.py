from rest_framework.routers import DefaultRouter
from .views import RouteViewSet

router = DefaultRouter()
router.register('routes', RouteViewSet)

urlpatterns = router.urls