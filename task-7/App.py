from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Handle messages
@socketio.on('message')
def handle_message(msg):
    print("📩 Received:", msg)
    send(msg, broadcast=True)  # send to all connected users

@app.route('/')
def index():
    return render_template('chat.html')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
