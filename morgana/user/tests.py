# Third party libreries
from django.test import TestCase

# Owns libraries
from .models import YelpUser
from .factories import YelpUserFactory
from api.factory_user import UserFactory
from .serializers import YelpUserSerializer
from rest_framework import status


# Create your tests here.
class YelpUserTestCase(TestCase):
    """Tests of the Business from api_yelp.  """
    
    def setUp(self) -> None:
        self.yelp_user = YelpUserFactory()
        self.serializer = YelpUserSerializer(instance=self.yelp_user)
    
    def test_model(self):
        """Test for string representation."""
        self.assertEqual(str(self.yelp_user), self.yelp_user.name)
    
    def test_model_fields(self):
        """Serializer data matches the Business object for each field."""
        for field_name in self.serializer.data.keys():
            self.assertEqual(
                self.serializer.data[field_name],
                getattr(self.yelp_user, field_name)
            )


class YelpUserViewsetTestCase(TestCase):
    """Viewset unit tests in django framework.  """
    def setUp(self):
        self.user = UserFactory()
        self.url = "/api/users/"

    def test_list_view(self):
        """Test that the list view works correctly"""
        data_fake = [YelpUserFactory(name=str(i)) for i in range(0, 4)]
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(business['user_id'] for business in response.data['results']),
            set(business.user_id for business in data_fake)
        )
    def test_get_detail(self):
        """GET a detail page for a Business."""
        business_fake = YelpUserFactory()
        response = self.client.get(f"{self.url}{business_fake.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], business_fake.name)
          
    def test_post(self):
        """POST to create a Business."""
        data = {
            "user_id": "11234567890",
            "name": "USER_TEST_01",
            "review_count": 2147483647,
            "useful": 2147483647,
            "funny": 2147483647,
            "cool": 2147483647,
            "fans": 2147483647,
            "elite": "string",
            "average_stars": 0,
            "compliment_hot": 2147483647,
            "compliment_more": 2147483647,
            "compliment_profile": 2147483647,
            "compliment_cute": 2147483647,
            "compliment_list": 2147483647,
            "compliment_note": 2147483647,
            "compliment_plain": 2147483647,
            "compliment_cool": 2147483647,
            "compliment_funny": 2147483647,
            "compliment_writer": 2147483647,
            "compliment_photos": 2147483647
        }
        self.assertEqual(YelpUser.objects.count(), 0)
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YelpUser.objects.count(), 1)
        business = YelpUser.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(business, field_name), data[field_name])
    
    def test_put(self):
        """PUT to update a Business."""
        business_fake = YelpUserFactory(user_id='11234567890')
        data = {
            "user_id": "11234567890",
            "name": "NEW_USER_TEST_01",
            "review_count": 123456789,
            "useful": 123456789,
            "funny": 123456789,
            "cool": 123456789,
            "fans": 123456789,
            "elite": "foo",
            "average_stars": 1,
            "compliment_hot": 123456789,
            "compliment_more": 123456789,
            "compliment_profile": 123456789,
            "compliment_cute": 123456789,
            "compliment_list": 123456789,
            "compliment_note": 123456789,
            "compliment_plain": 123456789,
            "compliment_cool": 123456789,
            "compliment_funny": 123456789,
            "compliment_writer": 123456789,
            "compliment_photos": 123456789
        }
        response = self.client.put(
            f"{self.url}{business_fake.user_id}/",
            data=data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)