"""
The flask application package.
"""

from flask import Flask


app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
import FlaskWebProject1.views


