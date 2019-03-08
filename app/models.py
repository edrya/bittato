from datetime import datetime
from app import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    fee = db.Column(db.String(64))
    variety = db.Column(db.String(128))
    market_price = db.Column(db.Integer)
    transaction_date = db.Column(db.DateTime)
    quantity = db.Column(db.String(128))
    location = db.Column(db.String(128))
    medium = db.Column(db.String(128))

    potato_id = db.Column(db.Integer, db.ForeignKey('potato.id'))

    def __repr__(self):
        return '<Transaction ID {}>'.format(self.id)


class Potato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variety_name = db.Column(db.String(128))
    product_id = db.Column(db.Integer, unique=True)
    country = db.Column(db.String(128))
    transactions = db.relationship('Transaction', backref='transaction', lazy='dynamic')

    def __repr__(self):
        return '<Potato Type {}>'.format(self.variety_name)
