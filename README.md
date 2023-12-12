Bloggy Flask

Bloggy Flask is a simple blogging web application built with Flask.

Table of Contents

## Introduction
## Features
## Prerequisites
## Getting Started
## Project Structure
## Database Setup
## Running the Application
## Testing
## Contributing
## License

## Introduction

Bloggy Flask is a web application that allows users to create, view, edit, and delete blog posts. It is built using the Flask web framework and follows a simple and modular structure.

## Features

User Authentication: Register, login, and logout functionality.
Create, View, Edit, and Delete Posts.
Simple and Responsive UI.
Unit Testing.

## Prerequisites

Before you begin, ensure you have the following installed:

Python 3.x
Flask
MySQL (or another relational database)
Virtualenv (recommended for creating a virtual environment)

## Getting Started

Clone the repository:

git clone https://github.com/niyioo/bloggy-flask.git

Navigate to the project directory:

cd bloggy-flask

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Project Structure

The project follows the following structure:

bloggy-flask/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   ├── comment.py
│   │   └── ...
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── posts.py
│   │   └── ...
│   ├── templates/
│   │   ├── index.html
│   │   ├── post_detail.html
│   │   └── ...
│   └── static/
│       ├── css/
│       ├── js/
│       ├── images/
│       └── ...
│
├── migrations/
│
├── tests/
│
├── venv/ (virtual environment)
│
├── requirements.txt
│
├── run.py
│
├── config.py
│
└── db/
    ├── __init__.py
    ├── models.py
    ├── migrations/
    │   ├── __init__.py
    │   └── ...
    └── config.py

## Database Setup

Set up your database server (e.g., MySQL).

Configure the database connection in config.py:

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/bloggy_db'

Initialize and migrate the database:

flask db init

flask db migrate -m "Initial database setup"

flask db upgrade

## Running the Application

Run the application using:

python run.py
Visit http://localhost:5000 in your browser.

## Testing

Run the tests using:

python -m unittest discover tests

## Contributing

If you'd like to contribute, please follow the Contributing Guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

theme: jekyll-theme-minimal

