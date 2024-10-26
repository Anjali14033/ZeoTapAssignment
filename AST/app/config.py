import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('AST_DB_SECRET_KEY')

    # Database settings (Using SQLite for simplicity)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ast.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
