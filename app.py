from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/image')
def show_image():
    return render_template('image.html')

@app.route('/next')
def next_image():
    # 在這裡處理切換下一張圖片的邏輯
    # 這裡只是簡單地示範，假設切換到下一張圖片的URL是/image
    return redirect(url_for('show_image'))

if __name__ == '__main__':
    app.run(debug=True)
