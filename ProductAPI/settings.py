# -*- coding: utf-8 -*-
import os

DATABASE = 'productsAPI'
DATABASE_HOST = os.environ['DB_PROYECTOX_PORT_27017_TCP_ADDR']
DATABASE_PORT = os.environ['DB_PROYECTOX_PORT_27017_TCP_PORT']
HOST = 'mongodb://%s:%s/%s' % (DATABASE_HOST, DATABASE_PORT, DATABASE)
