from flask import Flask, request
from flask_socketio import SocketIO, join_room, send
from .id_gen import gen_id

app = Flask(__name__, static_url_path='/static')

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def handle_message(data):
    print("received message: " + data)

@socketio.on("join")
def join(room=None):
    if room is None:
      room = gen_id()
    join_room(int(room))
    return room

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
