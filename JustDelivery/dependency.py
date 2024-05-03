import redis
from functools import lru_cache
from django.conf import settings


@lru_cache(maxsize=None)
def get_redis() -> redis.StrictRedis:
    return redis.StrictRedis(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
    )
