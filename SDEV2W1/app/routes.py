# Import the Flask application instance named 'app'
# This object was created in __init__.py
from app import app
from flask import render_template

# The @app.route decorator tells Flask which URL should trigger the function
# This route maps the root URL (http://localhost:5000/)
@app.route('/')

# Define a function named 'index'
# This function is called when a user visits '/'
def home():
    # Return a simple text response to be displayed in the browser
    return "Hello, From Lab Class Week 1!"

# Define a function named 'index'
# This function is called when a user visits '/index'
@app.route('/index')

def index():
    # Return the file index.html (in the templates folder)
    user = {'username': 'livguimaraes'}
    return render_template('index.html', webuser=user)