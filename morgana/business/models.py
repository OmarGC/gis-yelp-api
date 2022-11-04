from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Business(models.Model):
    business_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    point = gis_models.PointField(srid=4326, blank=True, null=True)
    stars = models.FloatField()
    review_count = models.PositiveIntegerField(default=0)
    is_open = models.PositiveIntegerField(default=0)
    attributes = models.JSONField(null=True)
    categories = models.TextField(null=True, blank=True)
    hours = models.JSONField(null=True)
    
    def __str__(self):
        return self.business_id + ' - ' + self.name