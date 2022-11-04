# Third party libreries
from rest_framework.routers import DefaultRouter

# Owns libraries
from .views import YelpUserViewSet

router = DefaultRouter()
router.register(r'', YelpUserViewSet, basename="users")

urlpatterns = router.urls