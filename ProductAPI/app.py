#!flask/bin/python
import pymongo
from bson.objectid import ObjectId
from flask import abort, Flask, jsonify, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.mongoengine import MongoEngine

from models import *


app = Flask(__name__)
# Mongo configuration
app.config['MONGODB_SETTINGS'] = {'DB': 'productsAPI'}
app.config['SECRET_KEY'] = "s3cr3tk3y"

db = MongoEngine(app)
# PyMongo Config
connection = pymongo.MongoClient('mongodb://localhost')
db_pymongo = connection.productsAPI
collection = db_pymongo.product

auth = HTTPBasicAuth()

# This sould be obtained by a database
@auth.get_password
def get_password(username):
    if username == 'manito':
        return 'proyectox'
    return None


@app.route('/proyectox/v1/products', methods=['GET'])
@auth.login_required
def get_products():
    try:
        # use of mongoengine
        products = [item.json() for item in Product.objects.all()]
        # products = [item for item in collection.find()] # use of pymongo
        if len(products) == 0:
            abort(404)
        return jsonify({'products': products})
    except:
        abort(500)


@app.route('/proyectox/v1/products/<string:product_id>', methods=['GET'])
@auth.login_required
def get_product(product_id):
    try:
        product = Product.objects.get(id=ObjectId(product_id))
        # product = collection.find_one({'_id': product_id})
        return jsonify({'product': product.json()})
    except Product.DoesNotExist:
        abort(404)
    except:
        abort(500)


@app.route('/proyectox/v1/products', methods=['POST'])
@auth.login_required
def add_product():
    try:
        if (not request.json or 'name' not in request.json or 'product_type'
                not in request.json):
            abort(404)

        product = Product(
            name=request.json['name'],
            product_type=request.json['product_type'],
            description=request.json['description'],
            price=request.json['price']
        )
        product.save()
        return jsonify(product.json()), 201
    except:
        abort(500)


@app.route('/proyectox/v1/products/<string:product_id>', methods=['PUT'])
@auth.login_required
def update_product(product_id):
    try:
        product = Product.objects.get(id=ObjectId(product_id))

        if not request.json:
            abort(404)
        if not request.json['name']:
            abort(500)
        if not request.json['product_type']:
            abort(500)

        product.name = request.json['name']
        product.product_type = request.json['product_type']
        product.description = (request.json['description'] if 'description'
                               in request.json else product.description)
        product.price = (request.json['price'] if 'price' in request.json
                         else product.price)
        product.save()
        return jsonify(product.json())
    except Product.DoesNotExist:
        abort(404)
    except:
        abort(500)


@app.route('/proyectox/v1/products/<string:product_id>', methods=['DELETE'])
@auth.login_required
def delete_product(product_id):
    try:
        product = Product.objects.get(id=ObjectId(product_id))

        product.delete()
        return jsonify({"result": True})
    except Product.DoesNotExist:
        abort(404)
    except:
        abort(500)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Server Error'}), 500)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run(debug=True)
