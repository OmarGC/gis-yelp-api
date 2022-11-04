# Third party libreries
from django.shortcuts import render
from rest_framework import viewsets, permissions
# Owns libraries
from .models import YelpUser
from .serializers import YelpUserSerializer

# Create your views here.
class YelpUserViewSet(viewsets.ModelViewSet):
    queryset = YelpUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = YelpUserSerializer
    