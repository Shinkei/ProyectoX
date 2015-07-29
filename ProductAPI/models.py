# -*- coding: utf-8 -*-
from app import db


class Store(db.Document):
    '''Model that represents a store'''
    name = db.StringField(max_length=255, required=True)
    address = db.StringField(max_length=255, required=True)
    phone = db.StringField(max_length=15, required=True)
    owner = db.StringField(max_length=255, required=True)
    geolocation = db.StringField(max_length=255, required=True)


class Product(db.Document):
    '''Model that represents a product, the relation in on the
       product document'''
    name = db.StringField(max_length=255, required=True)
    product_type = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255)
    price = db.FloatField()
    store = db.ReferenceField(Store)
    quantity = db.IntField()
    image = db.StringField(max_length=255, required=True)
