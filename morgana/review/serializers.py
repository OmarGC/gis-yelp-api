# Third party libreries
from rest_framework import serializers

# Owns libraries
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """This model is based on a previous model. 
        This class will convert a model into data 
        that will be able to be queried.  """
    class Meta:
        model = Review
        fields = (
            'review_id',
            'business_id',
            'user_id',
            'stars',
            'useful',
            'funny',
            'cool',
            'text',
            'date',
        )
        read_only_fields = ('text',)