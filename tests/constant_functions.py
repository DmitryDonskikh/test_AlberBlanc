import websockets
import asyncio
import json

data_1_id, data_1_phone, data_1_name, data_1_surname, data_1_age = '1', '1', 'John', 'Jones', 18
data_2_id, data_2_phone, data_2_name, data_2_surname, data_2_age = '2', '2', 'Peter', 'Peterson', 90
data_3_id, data_3_phone, data_3_name, data_3_surname, data_3_age = '3', '3', 'John', 'Smith', 44
data_4_id, data_4_phone, data_4_name, data_4_surname, data_4_age = '4', '4', 'Alex', 'Jones', 5


async def do_smth(dict):
    uri = "ws://127.0.0.1:4000"
    async with websockets.connect(uri) as ws:
        await ws.send(dict)
        repl = await ws.recv()
        return json.loads(repl)


def add(id, phone, name, surname, age):
        add_parameters = '{{"method": "add", ' \
                         '"id": "{id}", ' \
                         '"phone": "{phone}", ' \
                         '"name": "{name}", ' \
                         '"surname": "{surname}", ' \
                         '"age": {age}}}'.format(id=id, phone=phone, name=name, surname=surname, age=age)
        return asyncio.get_event_loop().run_until_complete(do_smth(add_parameters))


def add_kwargs(**data):
        add_parameters = '{"method": "add"'
        for key, value in data.items():
                if type(value) is int:
                        add_parameters += ', "{key}": {value}'.format(key=key, value=value)
                elif value is None:
                        add_parameters += ', "{key}": {value}'.format(key=key, value=value)
                else:
                        add_parameters += ', "{key}": "{value}"'.format(key=key, value=value)
        add_parameters += '}'
        return asyncio.get_event_loop().run_until_complete(do_smth(add_parameters))


def select_by_phone(id, phone):
        select_parameters = '{{"method": "select", "id": "{id}", "phone": "{phone}"}}'.format(id=id, phone=phone)
        return asyncio.get_event_loop().run_until_complete(do_smth(select_parameters))


def select_by_name(id, name):
        select_parameters = '{{"method": "select", "id": "{id}", "name": "{name}"}}'.format(id=id, name=name)
        return asyncio.get_event_loop().run_until_complete(do_smth(select_parameters))


def select_by_surname(id, surname):
        select_parameters = '{{"method": "select", "id": "{id}", "surname": "{surname}"}}'.format(id=id, surname=surname)
        return asyncio.get_event_loop().run_until_complete(do_smth(select_parameters))


def delete(id, phone):
    delete_parameters = '{{"method": "delete", "id": "{id}", "phone": "{phone}"}}'.format(id=id, phone=phone)
    return asyncio.get_event_loop().run_until_complete(do_smth(delete_parameters))


def update(id, phone, name, surname, age):
    update_parameters = '{{"method": "update", ' \
                        '"id": "{id}", "phone": ' \
                        '"{phone}", "name": "{name}", ' \
                        '"surname": "{surname}", ' \
                        '"age": {age}}}'.format(id=id, phone=phone, name=name, surname=surname, age=age)
    return asyncio.get_event_loop().run_until_complete(do_smth(update_parameters))
