from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)   
    phone = db.Column(db.String(15), unique=True, nullable=True)  
    gender = db.Column(db.String(10), nullable=False)
