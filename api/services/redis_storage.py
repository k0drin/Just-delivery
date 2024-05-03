from .order_container import Item


class RedisStorage:
    def __init__(self, conn):
        self.conn = conn

    def list_push(self, key, value):
        self.conn.lpush(key, value)

    def list_pop(self, key):
        return self.conn.lpop(key)
    
    def list_length(self, key):
        return self.conn.llen(key)
