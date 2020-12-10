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
    name = db.Column(db.String(1000))  # TODO if this is supposed to be a username it should also be labeled as unique
    balance = db.Column(db.Integer)
    tickets = db.Column(db.String(100))

class TicketInfo(db.Model):
    """
    A TicketInfo model which holds ticket informations
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(1000), unique=True) # based on our ticket buy the ticket must have a unique name
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.String(50))

    # this is if we only want the group of name and email to be unique
    '''
    __table_args__ = (db.UniqueConstraint('email', 'name', name='user_noSameName'),
                      )  # composite constraint can't have
    # both email and name be the same (ie a user has to name their sold tickets differently)
'''
# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
