from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Company Name: ABC Corporation <br> Location: India <br> Contact Detail: 999-999-9999"

@app.route("/welcome")
def welcomeP():
    return "<h1>Welcome to ABC Corporation</h1>"


@app.route("/abc")
def hello_world1():
    return "<h1>Hello, World!vjndjdv </h1>"

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "this is {}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")
