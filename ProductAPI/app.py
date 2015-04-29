# -*- coding: utf-8 -*-
# !flask/bin/python
from flask import Flask
from flask.ext.restful import Api
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

# Mongo configuration
app.config['MONGODB_SETTINGS'] = {'db': 'productsAPI'}
app.config['SECRET_KEY'] = "s3cr3tk3y"

db = MongoEngine(app)
