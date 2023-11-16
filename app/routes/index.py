# app/routes/index.py
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')  # You can customize this template name

@main.route('/about')
def about():
    return render_template('about.html')  # You can customize this template name

@main.route('/contact')
def contact():
    return render_template('contact.html')  # You can customize this template name
