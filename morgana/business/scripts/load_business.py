import json

from ..models import Business

def run():
    with open("business/scripts/business10k.json", "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            data = json.loads(line)
            
            if data.get('longitude') and data.get('latitude'):
                data.update({ 'point': f"POINT({data.get('longitude')} {data.get('latitude')})" })
                data.pop("longitude")
                data.pop("latitude")
            print(data)
            
            Business.objects.create(**data)