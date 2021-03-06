from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    nickname = db.Column(db.String(20), unique=True)
    blocked = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, default=datetime.now)
    modify_date = db.Column(db.DateTime, default=datetime.now)

    masters = db.relationship('Master', backref='user', lazy='dynamic')
    slaves = db.relationship('Slave', backref='user', lazy='dynamic')