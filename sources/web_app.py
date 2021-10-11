from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/test")
def test():
    return"<h>THIS IS A TEST</h>"

if __name__ == '__main__':
    app.run()

