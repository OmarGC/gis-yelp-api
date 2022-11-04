from django.db import models

from user.models import YelpUser
from business.models import Business


# Create your models here.
class Review(models.Model):
    review_id = models.CharField(max_length=22, primary_key=True)
    user_id = models.ForeignKey(
        YelpUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    business_id = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    stars = models.FloatField(default=0)
    useful = models.PositiveIntegerField(default=0)
    funny = models.PositiveIntegerField(default=0)
    cool = models.PositiveIntegerField(default=0)
    text = models.TextField()
    date = models.DateTimeField()
