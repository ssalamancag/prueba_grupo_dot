from app import db

class Quotation(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rate = db.Column(db.Float)
    max_amount = db.Column(db.Integer)

    def __init__(self, name, rate, max_amount):
        self.name = name
        self.rate = rate
        self.max_amount = max_amount

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'name': self.name,
           'rate': self.rate,
           'max_amount': self.max_amount
       }
