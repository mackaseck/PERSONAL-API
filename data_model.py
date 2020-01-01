from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String(50))
    DOB = db.Column(db.Integer)
    city = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def add_user(_first_name, _last_name, _DOB, _city, _email):
        new_user = User(first_name = _first_name, last_name = _last_name, DOB = _DOB, city = _city, email = _email)
        db.session.add(new_user)
        db.session.commit()


    def json(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "DOB": self.DOB, "city": self.city, "email": self.email}

    def get_all_users():
        return [user.json() for user in User.query.all()]

    def get_user(_email):
        user_to_return = User.json(User.query.filter_by(email= _email).first())
        return user_to_return

    def delete(_email):
        User.query.filter_by(email = _email).delete()
        db.session.commit()

    def update_user(_email, _city):
        user_to_update = User.query.filter_by(email = _email).first()
        user_to_update.city = _city
        db.session.commit()

    def replace_user(_first_name, _last_name, _DOB, _city, _email):
        user_to_replace = User.query.filter_by(email = _email).first()
        user_to_replace.first_name = _first_name
        user_to_replace.last_name = _last_name
        user_to_replace.DOB = _DOB
        user_to_replace.city = _city
        user_to_replace.email = _email
        db.session.commit()




    def __repr__(self):
        user_object = {'first_name': self.first_name, 'last_name': self.last_name, 'DOB': self.DOB, 'email': self.email}
        return json.dumps(user_object)

