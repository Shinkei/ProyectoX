# -*- coding: utf-8 -*-
# !flask/bin/python
from app import app
from product_api import ProductListAPI, ProductAPI
from store_api import StoreAPI, StoreListAPI
from flask.ext.restful import Api

api = Api(app)

api.add_resource(ProductListAPI, '/proyectox/v2/products', endpoint='products')
api.add_resource(ProductAPI, '/proyectox/v2/products/<string:id>',
                 endpoint='product')

api.add_resource(StoreListAPI, '/proyectox/v2/stores', endpoint='stores')
api.add_resource(StoreAPI, '/proyectox/v2/stores/<string:id>',
                 endpoint='store')

if __name__ == '__main__':
    app.run(debug=True)
