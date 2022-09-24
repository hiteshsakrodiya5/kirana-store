from service_objects.services import Service
from .models import Item

class AddItemService(Service):
    def process(self):
        name=self.data.get("name")
        price=self.data.get("price")
        description=self.data.get("description")
        category=self.data.get("category")
        item_create = Item.objects.create(
            name=name,
            category=category,
            price=price,
            description=description,
        )
        return item_create.name