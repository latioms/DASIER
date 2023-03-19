# import main flask librairies
from flask import Flask, render_template, request, redirect, url_for, flash

import os

# init app
app = Flask(__name__)

@app.route('/')
def index():
      # return render_template('index.html')
      return 'Hello World'

# @app.route('/diabetes')
# def diabetes():
#       return render_template('diabetes.html')