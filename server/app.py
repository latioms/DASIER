# import main flask librairies
from flask import Flask, render_template, request, redirect, url_for, flash

import os

# init app
app = Flask(__name__)

@app.route('/')
def index():
      # return render_template('index.html')
      return 'Hello World'

# run server
if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)