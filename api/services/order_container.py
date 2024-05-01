from JustDelivery.dependency import redis_connection as conn
from .redis_storage import RedisStorage

class Item:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity


class OrderContainer:
    def __init__(self, user_id, storage):
        self.user_id = user_id
        self.storage = storage

    def add_to_cart(self, item_id, quantity):
        item = Item(item_id, quantity)
        self.storage.list_push(f"cart:{self.user_id}", item)

    def remove_from_cart(self):
        return self.storage.list_pop(f"cart:{self.user_id}")


