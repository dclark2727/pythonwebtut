from logging.config import _LoggerConfiguration
from __init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')

class Shop(db.model):
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(150))
     image = db.Column(db.String(150))
     location = db.Column(db.String(150))
     rating = db.Column(db.String(150))
     reviews = db.Column(db.String(150))
     tags = db.Column(db.String(150))