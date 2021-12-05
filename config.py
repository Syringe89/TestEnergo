from os import environ

uvicorn_host = 'localhost'
uvicorn_port = 8000

host_server = environ.get('host_server', 'localhost')
db_server_port = environ.get('db_server_port', '5432')
database_name = environ.get('database_name', 'test_energo')
db_username = environ.get('db_username', 'postgres')
db_password = environ.get('db_password', 'postgres')
POSTGRESQL_URL = f'postgresql+asyncpg://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}'

redis_server = environ.get('redis_server', 'localhost')
redis_server_port = environ.get('redis_server_port', '6379')
REDIS_URL = f'redis://{redis_server}:{redis_server_port}'
