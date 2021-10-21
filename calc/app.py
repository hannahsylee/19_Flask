from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)
# Put your app in here.
@app.route('/add')
def add_function():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def subtract_function():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def multiply_function():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def divide_function():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)
    
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operator>')
def math_function(operator):
    """Do one of the math operations."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a,b)
    return str(result)

