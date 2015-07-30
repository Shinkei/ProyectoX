# -*- coding: utf-8 -*-
# !flask/bin/python
from app import auth
from models import Store

from bson.objectid import ObjectId
from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal

store_fields = {
    'id': fields.String,
    'name': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'owner': fields.String,
    'geolocation': fields.String
}


class StoreListAPI(Resource):
    '''Class that allow the usage of get a list of Stores and create a new
       store'''
    # Decorator that add the login verification
    decorators = [auth.login_required]

    def __init__(self):
        '''This method manage the fields verification in the class'''
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('address', type=str, required=True,
                                   location='json')
        self.reqparse.add_argument('owner', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('geolocation', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('phone', type=str, default="",
                                   location='json')
        super(StoreListAPI, self).__init__()

    def get(self):
        '''Get a list of Stores by the method get'''
        stores = Store.objects.all()
        return {'stores': [marshal(store, store_fields)
                for store in stores]}

    def post(self):
        '''Add a new store by the method post'''
        try:
            args = self.reqparse.parse_args()
            store = Store(
                name=args['name'],
                address=args['address'],
                phone=args['phone'],
                owner=args['owner'],
                geolocation=args['geolocation']
            )
            store.save()
            return {'store': marshal(store, store_fields)}, 201
        except Exception:
            abort(500)


class StoreAPI(Resource):
    '''Class that represents and allows the update, find and delete Stores by
       id'''
    # Decorator that add the login verification
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No store name provided',
                                   location='json')
        # self.reqparse.add_argument('product_type', type=str, required=True,
        #                            location='json')
        super(StoreAPI, self).__init__()

    def get(self, id):
        '''Find a store by id, using the http get method'''
        try:
            store = Store.objects.get(id=ObjectId(id))
            return {'store': marshal(store, store)}
        except Store.DoesNotExist:
            abort(404)
        except:
            abort(500)

    def put(self, id):
        '''Update a Store, giving the id and the new values, this use the
           http method PUT'''
        try:
            args = self.reqparse.parse_args()
            store = Store.objects.get(id=ObjectId(id))
            store.name = args['name']
            store.address = args['address']
            store.phone = (args['phone'] if 'phone'
                           in args else store.phone)
            store.owner = (args['owner'] if 'owner' in args
                           else store.owner)
            store.geolocation = (args['geolocation'] if 'geolocationgeolocation' in args
                                 else store.geolocation)
            store.save()
            return {'store': marshal(store, store_fields)}
        except Store.DoesNotExist:
            abort(404)
        except:
            abort(500)

    def delete(self, id):
        '''Delete a store by id, using the DELETE http method'''
        try:
            store = Store.objects.get(id=ObjectId(id))
            store.delete()
            return {'result': True}
        except Store.DoesNotExist:
            abort(404)
        except:
            abort(500)
