import json

from ..models import YelpUser


def run():
    with open("user/scripts/user100k.json", "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            data = json.loads(line)
            YelpUser.objects.create(**data)
