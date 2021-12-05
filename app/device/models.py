from sqlalchemy import Column, Integer, String, ForeignKey, Text, BigInteger
from sqlalchemy.dialects.postgresql import MACADDR
from sqlalchemy.orm import relationship

from app.device.db import Base


class Device(Base):
    __tablename__ = 'device'
    id = Column(BigInteger, primary_key=True)
    dev_type = Column(String(120))
    dev_id = Column(MACADDR)
    endpoint = relationship('Endpoint')


class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = Column(BigInteger, primary_key=True)
    device_id = Column(Integer, ForeignKey('device.id', ondelete='CASCADE', onupdate='CASCADE'))
    comment = Column(Text)
