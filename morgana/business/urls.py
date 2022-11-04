# Third party libreries
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# Owns libraries
from .views import BusinessViewSet

router = DefaultRouter()
router.register(r'', BusinessViewSet, basename='business')

urlpatterns = router.urls