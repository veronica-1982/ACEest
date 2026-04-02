from database import db
from datetime import datetime


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    program = db.Column(db.String(50))
    calories = db.Column(db.Integer)


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    week = db.Column(db.String(50))
    adherence = db.Column(db.Integer)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    workout = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)