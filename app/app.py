from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:interger>')
def count(interger):
    count = f''
    for i in range(interger):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        return f'{num1} + {num2} = {num1 + num2}'
    elif operation == '-':
        return f'{num1} - {num2} = {num1 - num2}'
    elif operation == '*':
        return f'{num1} * {num2} = {num1 * num2}'
    elif operation == 'div':
        return f'{num1} div {num2} = {num1 / num2}'
    elif operation == '%':
        return f'{num1} % {num2} = {num1 % num2}'
    else:
        return 'Invalid operation'


if __name__ == '__main__':
    app.run(port=5555, debug=True)