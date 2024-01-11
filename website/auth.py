from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login') # Login page URL
def login():
    return render_template("login.html")

@auth.route('/logout') # Logout page URL
def logout():
    return render_template("logout.html")

@auth.route('/sign-up') # Sign Up page URL
def sign_up():
    return render_template("sign_up.html")