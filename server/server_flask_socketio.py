from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['KEY'] = 'key'
socketIO = SocketIO(app, logger=True, engineio_logger=True)


@socketIO.on('message')
def handle_message(data):
    print("get" + data)

@socketIO.on('connect')
def test_connection():
    print("connected")

@socketIO.on('disconnect')
def disconnect():
    print('disc')


if __name__ == "__main__":
    socketIO.run(app, port=3000, host='0.0.0.0')