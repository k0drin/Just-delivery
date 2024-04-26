from dependency import *

class RedisStorage:
    def __init__(self):
        self.client = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
    
    def set_hash(self, key, field, value):
        """Sets a value in a hash stored in Redis."""
        self.client.hset(key, field, value)
    
    def get_hash(self, key):
        """Retrieves all fields and values from a hash stored in Redis."""
        return self.client.hgetall(key)
    
    def delete_hash_field(self, key, field):
        """Deletes a field from a hash stored in Redis."""
        self.client.hdel(key, field)

