from django.urls import path, include


urlpatterns = [
    path("users/", include("user.urls")),
    path("business/", include("business.urls")),
    path("reviews/", include("review.urls")),
]