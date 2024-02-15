from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_socketio.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)