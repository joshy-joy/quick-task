

from flask import Flask
from pymongo import MongoClient


#initialize app
app = Flask(__name__)


#importing configuration
app.config.from_pyfile('config.py')

#establishing connection to default mongo config "localhost:27017"
mongo = MongoClient('mongodb://localhost:27017/')

#importing views
from app import controller
