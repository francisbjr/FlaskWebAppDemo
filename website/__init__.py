from flask import Flask

def create_app():
    # Initialize app
    app = Flask(__name__)
    # Encrypt and secure key
    app.config['SECRET_KEY'] = 'johnny'

    # Import blueprints
    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app