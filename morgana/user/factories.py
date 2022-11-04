# Third party libreries
from factory.django import DjangoModelFactory
from factory import Faker, lazy_attribute
import faker

# Owns libraries
from user.models import YelpUser


class YelpUserFactory(DjangoModelFactory):    
    user_id = Faker('bothify', text='????#######?')
    name = Faker('name')
    review_count = Faker('random_digit')
    yelping_since = Faker('date_time_ad')
    useful = Faker('random_digit')
    funny = Faker('random_digit')
    cool = Faker('random_digit')
    fans = Faker('random_digit')
    friends = Faker('bothify', text='??????????????????????')
    elite = Faker('bothify', text='??????????????????????')
    average_stars = Faker('pyfloat', positive=True)
    compliment_hot = Faker('random_digit')
    compliment_more = Faker('random_digit')
    compliment_profile = Faker('random_digit')
    compliment_cute = Faker('random_digit')
    compliment_list = Faker('random_digit')
    compliment_note = Faker('random_digit')
    compliment_plain = Faker('random_digit')
    compliment_cool = Faker('random_digit')
    compliment_funny = Faker('random_digit')
    compliment_writer = Faker('random_digit')
    compliment_photos = Faker('random_digit')
    
    @lazy_attribute
    def yelping_since(self):
        fake = faker.Faker()
        
        return str(fake.date_time_ad())
    
    class Meta:
        model = YelpUser
        