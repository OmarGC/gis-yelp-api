import json

from ..models import Review
from user.models import YelpUser
from business.models import Business


def run():
    with open("review/scripts/review1M.json", "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            data = json.loads(line)
            try:
                user = YelpUser.objects.get(user_id=data["user_id"])
                data["user_id"] = user
            except YelpUser.DoesNotExist:
                data["user_id"] = None
            try:
                business = Business.objects.get(business_id=data["business_id"])
                data["business_id"] = business
            except Business.DoesNotExist:
                data["business_id"] = None
            Review.objects.create(**data)
