from qa327 import app
from flask_sqlalchemy import SQLAlchemy

"""
This file defines all models used by the server
These models provide us a object-oriented access
to the underlying database, so we don't need to 
write SQL queries such as 'select', 'update' etc.
"""


db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    """
    A user model which defines the sql table
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    balance = db.Column(db.Integer)
    tickets = db.Column(db.PickleType, nullable=False)


class UserInfo(db.Model):
    """
    A UserInfo model which hold user informations
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.String(50))

    data = []

    def __init__self(self):
        self.data.append(self)


class TicketInfo(db.Model):
    """
    A TicketInfo model which holds ticket informations
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.String(50))

    data = []

    def __init__self(self):
        self.data.append(self)
  
  
# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
