from app import db
from datetime import datetime as dt

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime)
    #instantiate this with name, description, price, tax. add a description area for the form, request it similar to the way that users are created through the register view
    #db.session.add for the product, passes in the product, db session.commit nothing gets passed in. p.save method insteead of db.sesion

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'tax': self.tax,
            'date_created': self.date_created
        }
        return data

    def from_dict(self, data):
        for field in ['name', 'description', 'price']:
            if field in data:
                setattr(self, field, data[field])
        self.tax = round(self.price * .06, 2)

    def __repr__(self):
        return f'{self.name} @{self.price}'