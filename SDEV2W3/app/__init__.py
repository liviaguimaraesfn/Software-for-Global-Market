#Start of code
from flask import Flask
from flask_babel import Babel

# Create an application object – instance of class Flask (imported at line 1)
app = Flask(__name__) # __name__ is a predefined Python variable – set to the name of the module in which it is used

# get_locale: a function which at the moment returns a 2 letter string code for a locale
def get_locale():
    return 'de'

#Hook Babel into your app - pass the app to Babel and pass the locale returned by get_locale to it – this will indicate translations to use
babel = Babel(app, locale_selector=get_locale)

# imports routes from the app (won’t exist when you start – you will create it)
from app import routes

#End of code