# save this as app.py
import flask
app = flask.Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"
@app.route('/index')
def index():
    return app_template('index.html')

if __name__ == '__main__':
    app.run()