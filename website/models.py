#SQL Schema
#***# Done #***#

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150))
    progressType = db.Column(db.String(150))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default= func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tickets = db.relationship('Ticket')

