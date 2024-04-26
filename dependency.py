import redis

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

redis_connection = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
