from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """
    returns 'welcome'
    """
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """
    returns 'welcome home'
    """
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """
    returns 'welcome back'
    """
    return "welcome back"

