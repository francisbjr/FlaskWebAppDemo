from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login') # Login page URL
def login():
    return render_template("login.jinja")

@auth.route('/logout') # Logout page URL
def logout():
    return "logout" #TODO: Render logout

@auth.route('/sign-up') # Sign Up page URL
def sign_up():
    return render_template("sign_up.jinja")