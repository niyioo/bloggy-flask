from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Initialize Flask-Login for user authentication
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Import routes and models after initializing extensions
from app.routes import auth, posts
from app.models import User, Post

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(posts)

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # Run the application
    app.run()
