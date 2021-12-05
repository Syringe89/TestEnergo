from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from config import POSTGRESQL_URL

engine = create_async_engine(POSTGRESQL_URL, echo=True, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
Base.metadata.bind = engine
