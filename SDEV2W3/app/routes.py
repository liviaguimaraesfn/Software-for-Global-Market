# Import the Flask application instance named 'app'
# This object was created in __init__.py
from app import app
from flask import render_template

# The @app.route decorator tells Flask which URL should trigger the function
# This route maps the root URL (http://localhost:5000/)
@app.route('/')

# Define a function named 'index'
# This function is called when a user visits '/index'
@app.route('/index')

def index():
    return render_template('index.html')