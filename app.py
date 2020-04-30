from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my broadcast event', namespace='/youtube')
def test_message2(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/youtube')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/youtube')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)