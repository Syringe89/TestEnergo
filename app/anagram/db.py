import aioredis

from config import REDIS_URL

redis = aioredis.from_url(REDIS_URL, db=0, encoding='utf-8',
                          decode_responses=True)
