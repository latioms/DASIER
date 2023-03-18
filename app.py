# import flask
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"

@app.post("/predict")
def predict():
   data = request.json

   try:
      sample = data['text']
   except KeyError:
      return jsonify({'error':'No text provided'})


# start the server
if __name__ == "__main__":
   app.run(debug=True)
