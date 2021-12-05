import os

import aioredis

redis_server = os.environ.get('redis_server', 'localhost')
redis_server_port = os.environ.get('redis_server_port', '6379')

redis = aioredis.from_url('redis://{}:{}'.format(redis_server, redis_server_port), db=0, encoding='utf-8',
                          decode_responses=True)
