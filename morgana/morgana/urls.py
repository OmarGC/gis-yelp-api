# Third party libreries
from django.contrib import admin
from django.urls import path, include

# Owns libraries
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=" GIS YELP API",
        default_version="v1",
        description="API example for morgana, this API has CRUD for the entities: Review, User, Business",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="omar.95gc@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path("", include(('api.urls', 'api'), namespace='api')),
        path('swagger/', schema_view.with_ui(cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui')
        ])),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
