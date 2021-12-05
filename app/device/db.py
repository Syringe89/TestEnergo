import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

host_server = os.environ.get('host_server', 'localhost')
db_server_port = os.environ.get('db_server_port', '5432')
database_name = os.environ.get('database_name', 'test_energo')
db_username = os.environ.get('db_username', 'postgres')
db_password = os.environ.get('db_password', 'postgres')
DATABASE_URL = 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port,
                                                            database_name)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession)
Base = declarative_base()
