from flask import Flask, request
from flask_socketio import SocketIO, join_room, send
from .manage_rooms import make_room, rooms, RoomDoesNotExist
from .room import RoomState

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def handle_message(data):
    print("received message: " + data)


@socketio.on("join")
def join(room_id):
    try:
        room = rooms[room_id]
    except KeyError:
        raise RoomDoesNotExist
    if room.state is RoomState.FETUS:
        room.state = RoomState.WAITING
    join_room(room.id)
    return room.asdict()


@app.route("create", methods=["POST"])
def create():
    room = make_room()
    return room.asdict()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
