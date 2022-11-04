# Third party libreries
from django.shortcuts import render
from rest_framework import viewsets, permissions
# Owns libraries
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewSerializer
    