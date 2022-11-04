# Third party libreries
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# Owns libraries
from .models import Business
from .serializers import BusinessSerializer


# Create your views here.
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BusinessSerializer
    max_page_size = 1000
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['point']
    
    
    @action(detail=False)
    def get_business_from_distance(self, request):
        """
        This method calculates businesses within a radius of 1 km 
        by default but you can send the distance in KM as a parameter. 
        
        Args:
            lat (float): [Latitude]
            long (float): [Longitude]
            radius (int): [Radius]
            
        Returns:
            List of businesses in the area
        """
        
        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)
        radius = self.request.query_params.get('radius', 1)
        
        if not (long or lat):
            return Response({"message": "Required field not found."},
                                        status=status.HTTP_404_NOT_FOUND)
        
        point = GEOSGeometry(f"POINT({long} {lat})", srid=4326)
        p = Business.objects.filter(point__distance_lt=(point, D(km=radius)))
        serializer = self.get_serializer(p, many=True)
        
        return Response({"data": serializer.data})
    