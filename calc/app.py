from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/math/<operation>')
def main(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    if operation == 'add':
        return f"<h1>Result: {str(operations.add(a, b))}</h1>"
    elif operation == 'sub':
        return f"<h1>Result: {str(operations.sub(a, b))}</h1>"
    elif operation == 'mult':
        return f"<h1>Result: {str(operations.mult(a, b))}</h1>"
    elif operation == 'div':
        return f"<h1>Result: {str(operations.div(a, b))}</h1>"
    else:
        return f"Invalid Opeartion: {operation}"