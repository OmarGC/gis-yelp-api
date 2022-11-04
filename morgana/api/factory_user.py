# Third party libreries
from factory.django import DjangoModelFactory
from factory import Faker, lazy_attribute
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Owns libraries


class UserFactory(DjangoModelFactory):
    is_active = True
    username = Faker('first_name')
    email = Faker('free_email')
    password = make_password("password")
    is_staff = True
    is_superuser = True
    
    
    class Meta:
        model = User
        