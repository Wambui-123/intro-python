from flask import Flask

app = Flask(__name__)

@app.route('/')

def intro():
    return "My first flask application"