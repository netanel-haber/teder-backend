from random import randint
from .room import Room
from typing import Dict


rooms: Dict[str, Room] = {}

start, end = 100000, 999999
MAX_ROOMS = (end - start) / 2


def room_exists(room_id):
    return room_id in rooms


def make_room():
    if len(rooms) >= MAX_ROOMS:
        raise RoomCapacityExceeded
    room_id = str(randint(start, end))
    if not room_exists(room_id):
        room = Room(room_id)
        rooms[room_id] = room
        return room
    return make_room()


class RoomCapacityExceeded(Exception):
    pass


class RoomDoesNotExist(Exception):
    pass
