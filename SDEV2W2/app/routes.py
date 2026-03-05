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

# only calling from index (not function home) because it is applied to all pages

def index(): # view function
    # Return the file index.html (in the templates folder)
    user = {'username': 'livguimaraes'}
    labclasses = [
        {
            'weekno': 'one',
            'content': 'Getting started with Flask!'
        },
        {
            'weekno': 'two',
            'content': 'Template Inheritance!'
        }
    ]
    return render_template('index.html', pagetitle='Lab TWO', webuser = user, labclasses = labclasses)

# Route to labs.html template
@app.route('/labs')
# View which renders this template in response to a request, USING return render_template
def labs():
    return render_template('labs.html', pagetitle='Lab Classes')

# Route to ca.html template
@app.route('/ca')
# View which renders this template in response to a request
def ca():
    return render_template('ca.html', pagetitle='CA')