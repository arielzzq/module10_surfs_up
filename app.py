# import the flask dependency
from flask import Flask

#create a new flask app instance
app = Flask(__name__)

#create flask routes
@app.route('/')
#The forward slash is commonly known as the highest level of hierarchy in any computer system.
def hello_world():
    return 'Hello world'



