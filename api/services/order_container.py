import json
from dataclasses import dataclass
from JustDelivery.dependency import redis_connection as conn


@dataclass
class Item:
    item_id: str
    quantity: int

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data: str) -> 'Item':
        data = json.loads(json_data)
        return cls(**data)


class OrderContainer:
    def __init__(self, user_id, storage):
        self.user_id = user_id
        self.storage = storage

    def add_to_cart(self, item_id, quantity):
        from .redis_storage import RedisStorage
        item = Item(item_id, quantity)
        self.storage.list_push(f"cart:{self.user_id}", item.to_json())

    def remove_from_cart(self):
        from .redis_storage import RedisStorage # For fix circular import
        return self.storage.list_pop(f"cart:{self.user_id}")


