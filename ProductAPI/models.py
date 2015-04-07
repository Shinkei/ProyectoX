from app import db
from flask import url_for


class Product(db.Document):
    name = db.StringField(max_length=255, required=True)
    product_type = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255)
    price = db.FloatField()

    def json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "product_type": self.product_type,
            "description": self.description,
            "price": self.price,
            "uri": url_for('get_product', product_id=str(self.id), _external=True)
        }
