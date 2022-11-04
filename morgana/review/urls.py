from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename="review")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
