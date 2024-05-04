import json
from dataclasses import dataclass

@dataclass
class Item:
    item_id: str
    quantity: int 

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data: str) -> "Item":
        data = json.loads(json_data)
        return cls(**data)


class OrderContainer:
    def __init__(self, user_id, storage):
        self.user_id = user_id
        self.storage = storage

    def add_to_cart(self, item_id, quantity):
        item = Item(item_id, quantity)
        self.storage.list_push(f"cart:{self.user_id}", item.to_json())

    def remove_from_cart(self, item_id, quantity):
        item = Item(item_id, quantity)
        return self.storage.list_pop(f"cart:{self.user_id}")
    
    def get_order_items(self):
        cart_key = f"cart:{self.user_id}"
        order_items = {}

        all_items_json = self.storage.list_range(cart_key, 0, -1)

        for item_json in all_items_json:
            item = Item.from_json(item_json)
            order_items[item.item_id] = order_items.get(item.item_id, 0) + item.quantity

        return order_items
       
