# -*- coding: utf-8 -*-
# !flask/bin/python
import settings

from flask import Flask, jsonify, make_response

from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'manito':
        return 'proyectox'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


# Mongo configuration
app.config['MONGODB_SETTINGS'] = {'db': settings.DATABASE, 'host':'mongodb://localhost:27017/productsAPI'}#'host':'mongodb://172.17.0.7:27017/productsAPI'}
app.config['SECRET_KEY'] = "s3cr3tk3y"

db = MongoEngine(app)
