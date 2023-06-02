#This is an example of Many to Many relationship between tables;

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
app.config['DEBUG'] = True
db = SQLAlchemy(app)

order_items = db.Table('order_items', 
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id',db.Integer, db.ForeignKey('product.id'), primary_key=True)
)
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(), nullable=False)
    products = db.relationship('Product', secondary=order_items, 
        backref=db.backref('orders', lazy=True))
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run()