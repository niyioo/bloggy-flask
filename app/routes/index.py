# app/routes/index.py
from flask import Blueprint, render_template
from app.models.post import Post  # Import the Post model

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Retrieve all posts from the database
    posts = Post.query.all()

    # Pass the posts to the template
    return render_template('main/home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
