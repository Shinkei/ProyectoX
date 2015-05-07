# -*- coding: utf-8 -*-
# !flask/bin/python
from app import auth, api, app
from models import Product

from bson.objectid import ObjectId
from flask import jsonify, abort, make_response
from flask.ext.restful import Resource, reqparse, fields, marshal


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

product_fields = {
    'id': fields.String,
    'name': fields.String,
    'product_type': fields.String,
    'description': fields.String,
    'price': fields.Float
}


class ProductListAPI(Resource):
    '''Class that allow the usage of get a list of Products and create a new
       product'''
    # Decorator that add the login verification
    decorators = [auth.login_required]

    def __init__(self):
        '''This method manage the fields verification in the class'''
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('product_type', type=str, required=True,
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('price', type=int, default=0,
                                   location='json')
        super(ProductListAPI, self).__init__()

    def get(self):
        '''Get a list of Products by the method get'''
        products = Product.objects.all()
        return {'products': [marshal(product, product_fields)
                for product in products]}

    def post(self):
        '''Add a new product by the method post'''
        try:
            args = self.reqparse.parse_args()
            product = Product(
                name=args['name'],
                product_type=args['product_type'],
                description=args['description'],
                price=args['price']
            )
            product.save()
            return {'product': marshal(product, product_fields)}, 201
        except Exception:
            abort(500)


class ProductAPI(Resource):
    '''Class that represents and allows the update, find and delete Products by
       id'''
    # Decorator that add the login verification
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('product_type', type=str, required=True,
                                   location='json')
        super(ProductAPI, self).__init__()

    def get(self, id):
        '''Find a product by id, using the http get method'''
        try:
            product = Product.objects.get(id=ObjectId(id))
            return {'product': marshal(product, product_fields)}
        except Product.DoesNotExist:
            abort(404)
        except:
            abort(500)

    def put(self, id):
        '''Update a Product, giving the id and the new values, this use the
           http method PUT'''
        try:
            args = self.reqparse.parse_args()
            product = Product.objects.get(id=ObjectId(id))
            product.name = args['name']
            product.product_type = args['product_type']
            product.description = (args['description'] if 'description'
                                   in args else product.description)
            product.price = (args['price'] if 'price' in args
                             else product.price)
            product.save()
            return {'product': marshal(product, product_fields)}
        except Product.DoesNotExist:
            abort(404)
        except:
            abort(500)

    def delete(self, id):
        '''Delete a product by id, using the DELETE http method'''
        try:
            product = Product.objects.get(id=ObjectId(id))
            product.delete()
            return {'result': True}
        except Product.DoesNotExist:
            abort(404)
        except:
            abort(500)

api.add_resource(ProductListAPI, '/proyectox/v2/products', endpoint='products')
api.add_resource(ProductAPI, '/proyectox/v2/products/<string:id>',
                 endpoint='product')

if __name__ == '__main__':
    app.run(debug=True)
