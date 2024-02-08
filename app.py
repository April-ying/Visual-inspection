from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# 假設您有一個圖片URL的列表
image_urls = ['/static/image1.jpg', '/static/image2.jpg', '/static/image3.jpg']
current_image_index = 0

# 主頁面
@app.route('/')
def index():
    return render_template('index_socketio.html')

# 顯示圖片的頁面
@app.route('/image')
def show_image():
    return render_template('image_socketio.html', current_image=image_urls[current_image_index])

# 下一張圖片的確認頁面
@app.route('/next')
def next_image_page():
    return render_template('next_socketio.html')

# 當確認切換到下一張圖片時的事件處理
@socketio.on('confirm_next_image')
def confirm_next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_urls)
    new_image_url = image_urls[current_image_index]
    # 發送更新圖片URL的事件
    socketio.emit('update_image', {'image_url': new_image_url}, broadcast=True)
    # 發送等待確認的事件
    socketio.emit('wait_for_confirmation', broadcast=True)

# 主程式入口
if __name__ == '__main__':
    socketio.run(app, debug=True)
