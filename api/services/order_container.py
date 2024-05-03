import json
from dataclasses import dataclass

@dataclass
class Item:
    item_id: str
    #quantity: int # temporarily : )

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

    def remove_from_cart(self, item_id):
        item = Item(item_id)
        return self.storage.list_pop(f"cart:{self.user_id}")
    
    def get_order_items(self):
        cart_key = f"cart:{self.user_id}"
        order_items = {}

        # Получение длины списка корзины
        cart_length = self.storage.list_length(cart_key)

        # Получение всех элементов корзины
        for index in range(cart_length):
            item_json = self.storage.list_get(cart_key, index)
            item_data = json.loads(item_json)
            item_id = item_data.get("item_id")
            quantity = item_data.get("quantity", 0)
            order_items[item_id] = order_items.get(item_id, 0) + quantity

        return order_items
       
