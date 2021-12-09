from sqlalchemy import Column, Integer, String, ForeignKey, Text, BigInteger
from sqlalchemy.dialects.postgresql import MACADDR
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index

from app.device.db import Base


class Device(Base):
    __tablename__ = 'device'
    id = Column(BigInteger, primary_key=True)
    dev_type = Column(String(120))
    dev_id = Column(MACADDR)
    endpoint = relationship('Endpoint')


Index('devices_dev_id_dev_type_index', Device.dev_id, Device.dev_type)


class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = Column(BigInteger, primary_key=True)
    device_id = Column(Integer, ForeignKey('device.id', ondelete='CASCADE', onupdate='CASCADE'))
    comment = Column(Text)
