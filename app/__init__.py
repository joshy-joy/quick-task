from flask import Flask
from pymongo import MongoClient
from flask_httpauth import HTTPTokenAuth


#initialize app
app = Flask(__name__)


#importing configuration
app.config.from_pyfile('config.py')

#establishing connection to default mongo config "localhost:27017"
mongo = MongoClient('mongodb://localhost:27017/')

tokens = {"B1n0FlddHVnfBLeAkC": "admin"}

#Http Authentication
auth = HTTPTokenAuth(scheme='Bearer')

#importing views
from app import controller
