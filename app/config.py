import os
from datetime import timedelta

class Config:
    # Set the secret key for secure session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f5c3e567c0ed0926e39612cca820de88'

    # Configure the MySQL database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql://bloggy:blog@localhost/bloggy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configure other application settings if needed
    DEBUG = False  # Set to False in production
    TESTING = False
    JSON_SORT_KEYS = False  # Maintain order of keys in JSON responses
    SESSION_COOKIE_SECURE = True  # Set to True for HTTPS only
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)  # Set session expiration time

    # Flask-Mail settings for email functionality
    # (Add these if you plan to implement email features)
    # MAIL_SERVER = 'smtp.example.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'your_username'
    # MAIL_PASSWORD = 'your_password'
