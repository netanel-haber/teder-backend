from random import randint

rooms = set()

start, end = 100000, 999999
MAX_ROOMS = (end - start) / 2


class RoomCapacityExceeded(Exception):
    pass


def gen_id():
    value = randint(start, end)
    if value not in rooms:
        rooms.add(value)
        return str(value)
    if len(rooms) >= MAX_ROOMS:
        raise RoomCapacityExceeded
    return gen_id()

