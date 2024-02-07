from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_socketio.html')

@app.route('/image')
def show_image():
    return render_template('image_socketio.html')

@socketio.on('next_image_event')
def next_image():
    # 在這裡處理切換下一張圖片的邏輯
    # 這裡只是簡單地示範，假設切換到下一張圖片的URL是/image
    socketio.emit('redirect', {'url': '/image'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)