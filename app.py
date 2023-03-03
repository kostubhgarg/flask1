from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_operation():
    if(request.method =='POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops =='add'):
            r = num1+num2
            result = 'The result of '+ str(num1) + ' + ' + str(num2) +' is equal to ' +str(r)
        if(ops =='subtract'):
            r = num1-num2
            result = 'The result of '+ str(num1) + ' - ' + str(num2) +' is equal to ' +str(r)
       
        if(ops =='multiply'):
            r = num1*num2
            result = 'The result of '+ str(num1) + ' X ' + str(num2) +' is equal to ' +str(r)
        
        if(ops =='divide'):
            r = num1/num2
            result = 'The result of '+ str(num1) + ' / ' + str(num2) +' is equal to ' +str(r)
        return render_template('results.html', result = result)


# @app.route("/")
# def hello_world():
#     return "Company Name: ABC Corporation <br> Location: India <br> Contact Detail: 999-999-9999"

# @app.route("/welcome")
# def welcomeP():
#     return "<h1>Welcome to ABC Corporation</h1>"

# @app.route("/new")
# def test():
#     return "abc"
# @app.route("/abc")
# def hello_world1():
#     return "<h1>Hello, World!vjndjdv </h1>"

# @app.route("/test2")
# def test2():
#     data = request.args.get('x')
#     return "this is {}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")
