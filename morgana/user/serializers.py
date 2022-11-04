# Third party libreries
from rest_framework import serializers

# Owns libraries
from .models import YelpUser

class YelpUserSerializer(serializers.ModelSerializer):
    """This model is based on a previous model. 
        This class will convert a model into data 
        that will be able to be queried.  """
    class Meta:
        model = YelpUser
        fields = (
            'user_id',
            'name',
            'review_count',
            'useful',
            'funny',
            'cool',
            'fans',
            'elite',
            'average_stars',
            'compliment_hot',
            'compliment_more',
            'compliment_profile',
            'compliment_cute',
            'compliment_list',
            'compliment_note',
            'compliment_plain',
            'compliment_cool',
            'compliment_funny',
            'compliment_writer',
            'compliment_photos',
        )
        read_only_fields = ('yelping_since',)