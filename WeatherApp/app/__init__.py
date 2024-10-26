from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates',static_folder='../static')

    # Configurations
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
