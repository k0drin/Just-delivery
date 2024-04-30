from JustDelivery.dependency import redis_connection as conn
from .redis_storage import RedisStorage


class OrderContainer:
    def __init__(self, user_id, storage):
        self.user_id = user_id
        self.storage = storage
    
    def add_item(self, item_id, quantity):
        """ Adds an item with a specific quantity to the order. """
        self.storage.set_hash(f"order:{self.user_id}", item_id, quantity)
    
    def remove_item(self, item_id):
        """ Removes an item from the order. """
        self.storage.delete_hash_field(f"order:{self.user_id}", item_id)
    
    def get_order_items(self):
        """ Returns all items and their quantities in the order. """
        return self.storage.get_hash(f"order:{self.user_id}")


