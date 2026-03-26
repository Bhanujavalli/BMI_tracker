import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-bmi'
    # Defaulting to SQLite for easy local setup, easily swappable to MySQL
    # Just update the string to 'mysql+pymysql://username:password@localhost/bmi_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'bmi_tracker.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
