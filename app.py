# config                    
from flask import Flask
app = Flask(__name__)

#Home Route
@app.route('/')
def index():
    return 'Hello, this is PetFax.'

#Pet Index Route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'