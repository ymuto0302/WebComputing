from flask import Flask

application = Flask(__name__)

#default
@application.route('/')
def index():
    return "Hello Flask"
