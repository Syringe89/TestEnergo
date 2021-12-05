from random import choice, randint

from sqlalchemy import select
from sqlalchemy.sql.functions import count

from app.device.db import async_session
from app.device.models import Device, Endpoint


async def create_new_endpoints_db(new_endpoint: Endpoint):
    async with async_session() as session:
        await session.merge(new_endpoint)
        await session.commit()


async def create_new_device_db(new_device: Device):
    async with async_session() as session:
        await session.merge(new_device)
        await session.commit()


async def get_devices_without_endpoint_db():
    async with async_session() as session:
        devices = await session.execute(
            select(Device.dev_type, count(Device.id).label('number_of_devices')).join(Endpoint,
                                                                                      isouter=True).where(
                Endpoint.device_id.is_(None)).group_by(Device.dev_type))
    return devices


def generate_dev_type() -> str:
    return choice(['emeter', 'zigbee', 'lora', 'gsm'])


def generate_macaddr() -> str:
    return ':'.join(['%02x' % randint(0x00, 0xff) for _ in range(6)])
