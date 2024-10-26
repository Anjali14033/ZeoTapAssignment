from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    # Load configurations from config.py
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
