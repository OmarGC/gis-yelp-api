# Third party libreries
from factory.django import DjangoModelFactory
from factory import Faker, lazy_attribute
import faker

# Owns libraries
from business.models import Business


class BusinessFactory(DjangoModelFactory):
    business_id = Faker('bothify', text='????#######?')
    name = Faker('company')
    address = Faker('street_address')
    city = Faker('city')
    state = Faker('city')
    postal_code = Faker('postcode')
    stars = Faker('random_digit')
    review_count = Faker('random_digit')
    is_open = Faker('random_element', elements=(1,2))
    
    
    @lazy_attribute
    def point(self):
        fake = faker.Faker()
        location_fake = fake.location_on_land(coords_only=True)
        return f"POINT({location_fake[1]} {location_fake[0]})" 
    
    class Meta:
        model = Business
        