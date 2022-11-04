# Third party libreries
from django.test import TestCase

# Owns libraries
from .models import Business
from .factories import BusinessFactory
from api.factory_user import UserFactory
from .serializers import BusinessSerializer
from rest_framework import status


# Create your tests here.
class BusinessTestCase(TestCase):
    """Tests of the Business from api_yelp.  """
    
    def setUp(self) -> None:
        self.business = BusinessFactory()
        self.serializer = BusinessSerializer(instance=self.business)
    
    def test_model(self):
        """Test for string representation."""
        self.assertEqual(str(self.business), f"{self.business.business_id} - {self.business.name}")
    
    def test_model_fields(self):
        """Serializer data matches the Business object for each field."""
        for field_name in self.serializer.data.keys():
            self.assertEqual(
                self.serializer.data[field_name],
                getattr(self.business, field_name)
            )

class BusinessViewsetTestCase(TestCase):
    """Viewset unit tests in django framework.  """
    def setUp(self):
        self.user = UserFactory()
        self.url = "/api/business/"
       
    def test_business_from_distance(self):
        """Test get the business within a radius of 2 km.  
            Since the test db is empty, it returns 0.  """
        response = self.client.get(f"{self.url}?lat=33.5221425&long=-112.0184807&radius=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_view(self):
        """Test that the list view works correctly"""
        business_fake = [BusinessFactory(name=str(i)) for i in range(0, 4)]
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(business['business_id'] for business in response.data['results']),
            set(business.business_id for business in business_fake)
        )
    
    def test_get_detail(self):
        """GET a detail page for a Business."""
        business_fake = BusinessFactory()
        response = self.client.get(f"{self.url}{business_fake.business_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], business_fake.name)
          
    def test_post(self):
        """POST to create a Business."""
        data = {
            "business_id": "TEST1h84yJXfytovILXOAQ",
            "name": "Arizona Biltmore Golf Club",
            "address": "2818 E Camino Acequia Drive",
            "city": "Phoenix",
            "state": "AZ",
            "postal_code": "85016",
            "point": "SRID=4326;POINT(-112.0184807 33.5221425)",
            "stars": 3.0,
            "review_count": 5,
            "is_open": 0
        }
        self.assertEqual(Business.objects.count(), 0)
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Business.objects.count(), 1)
        business = Business.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(business, field_name), data[field_name])
            
    def test_put(self):
        """PUT to update a Business."""
        business_fake = BusinessFactory(business_id='TEST1h84yJXfytovILXOAQ')
        data = {
            "business_id": "TEST1h84yJXfytovILXOAQ",
            "name": "Arizona Biltmore Golf Club",
            "address": "2818 E Camino Acequia Drive",
            "city": "NEW CITY",
            "state": "AZ",
            "postal_code": "85016",
            "point": "SRID=4326;POINT(-112.0184807 33.5221425)",
            "stars": 3.0,
            "review_count": 5,
            "is_open": 0
        }
        response = self.client.put(
            f"{self.url}{business_fake.business_id}/",
            data=data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
