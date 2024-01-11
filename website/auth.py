from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login') # Login page URL
def login():
    return "<p>Login</p>"

@auth.route('/logout') # Logout page URL
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up') # Sign Up page URL
def sign_up():
    return "<p>Sign Up</p>"