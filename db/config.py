import os

class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql://bloggy:blog@localhost/bloggy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
