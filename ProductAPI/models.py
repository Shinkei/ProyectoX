# -*- coding: utf-8 -*-
from app import db


class Product(db.Document):
    '''Model that represents a product'''
    name = db.StringField(max_length=255, required=True)
    product_type = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255)
    price = db.FloatField()
