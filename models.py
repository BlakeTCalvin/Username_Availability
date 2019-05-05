from flask import flash, session
from sqlalchemy.sql import func
from config import db, EMAIL_REGEX, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    email = db.Column(db.String(60))
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    @classmethod
    def validate_user(cls, user_data):
        is_valid = True
        if len(user_data['first_name']) < 1:
            is_valid = False
            flash("Please provide a first name!")
        if not EMAIL_REGEX.match(user_data['email']):
            is_valid = False
            flash("Please provide a valid email address!")
        if len(user_data['username']) < 1:
            is_valid = False
            flash("Please provide a username!")
        if len(user_data['password']) < 5:
            is_valid = False
            flash("Password must be at least 5 characters!")
        if user_data['password'] != user_data['cpassword']:
            is_valid = False
            flash("Passwords do not match!")
        return is_valid

    @classmethod 
    def add_new_user(cls, user_data):
        hashed_password = bcrypt.generate_password_hash(user_data['password'])
        user_to_add = cls(first_name=user_data['first_name'], email=user_data['email'], username=user_data['username'], password=hashed_password)
        db.session.add(user_to_add)
        db.session.commit()
        return user_to_add