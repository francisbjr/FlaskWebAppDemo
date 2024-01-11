from flask import Flask

def create_app():
    # Initialize app
    app = Flask(__name__)
    # Encrypt and secure key
    app.config['SECRET_KEY'] = 'johnny'

    return app