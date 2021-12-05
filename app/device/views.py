from copy import copy
from random import shuffle
from typing import List

from fastapi import APIRouter

from app.device.models import Device, Endpoint
from app.device.services import generate_dev_type, generate_macaddr, create_new_device_db, create_new_endpoints_db, \
    get_devices_without_endpoint_db

router_device = APIRouter()


@router_device.post('/add_devices', status_code=201)
async def add_devices() -> List[Device]:
    list_of_devices = []
    for i in range(10):
        new_device = Device(id=i,
                            dev_type=generate_dev_type(),
                            dev_id=generate_macaddr())
        list_of_devices.append(new_device)
        await create_new_device_db(new_device)

    list_of_endpoints = []
    shuffled_list_of_devices = list(range(10))
    shuffle(shuffled_list_of_devices)
    for i in range(5):
        new_endpoint = Endpoint(id=i, device_id=shuffled_list_of_devices[i],
                                comment=f'point to {shuffled_list_of_devices[i]} device')
        list_of_endpoints.append(new_endpoint)
        await create_new_endpoints_db(new_endpoint)

    return {'list_of_devices:': list_of_devices, 'list_of_ednpoints:': list_of_endpoints}


@router_device.get('/get_devices_without_endpoint')
async def get_devices_without_endpoint():
    result = await get_devices_without_endpoint_db()
    return {'devices_without_endpoint:': list(result)}
