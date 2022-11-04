# Third party libreries
from rest_framework import serializers

# Owns libraries
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    """This model is based on a previous model. 
        This class will convert a model into data 
        that will be able to be queried.  """
    class Meta:
        """Put the model and below the fields that are going to be consulted.  
            in read_only_fields, you have to put the read-only fields"""
        model = Business
        fields = (
            'business_id',
            'name',
            'address',
            'city',
            'state',
            'postal_code',
            'point',
            'stars',
            'review_count',
            'is_open',
        )
        read_only_fields = ('is_open',)