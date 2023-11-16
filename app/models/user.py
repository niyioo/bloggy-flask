from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define a relationship with the Post model
    posts = db.relationship('Post', back_populates='author')

    def set_password(self, password):
        # Assuming the provided password is already hashed
        self.password = password

    def check_password(self, password):
        return self.password == password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
