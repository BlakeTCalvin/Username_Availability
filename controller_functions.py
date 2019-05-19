from flask import render_template, redirect, request, session, flash, jsonify
from config import db, bcrypt
from models import User
import re

def index():
    get_all_users = User.query.all()
    return render_template("index.html", users=get_all_users)

def register():
    validation_check = User.validate_user(request.form)
    if not validation_check:
        return redirect("/")
    else:
        new_user = User.add_new_user(request.form)
        session['user_id'] = new_user.id
        session['first_name'] = new_user.first_name
    return redirect("/")

def username():
    found = False
    check_username = User.query.filter_by(username = request.form['username']).all()
    if check_username:
        found = True
    return render_template("partials/username.html", found=found)

def usersearch():
    username = request.args.get("username")
    users = User.query.filter(User.username.startswith(username)).all()
    print(users)
    return render_template("partials/usersearch.html", users=users)