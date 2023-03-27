# import main flask librairies
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pickle as pkl
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'diabetes.pkl')

with open(file_path, 'rb') as f:
      diabetes_model = pkl.load(f)

# init app
app = Flask(__name__)

###############################################
# PROCESSING
###############################################
def predict_diabetes(tab):
      pred = diabetes_model.predict(tab)
      return pred

###############################################
# ROUTES
###############################################
@app.route('/')
def index():
      return render_template('index.html')

# route de loan
@app.route('/loan', methods=['GET', 'POST'])
def loan():
      if request.method == 'POST':
            # get form data
            loan_amount = request.form['loan_amount']
            loan_term = request.form['loan_term']
            interest_rate = request.form['interest_rate']
            # calculate monthly payment
            monthly_payment = float(loan_amount) * (float(interest_rate) / 100) / (1 - (1 + float(interest_rate) / 100) ** (-float(loan_term)))
            # format monthly payment to 2 decimal places
            monthly_payment = "{:.2f}".format(monthly_payment)
            # return monthly payment
            return render_template('loan.html', monthly_payment=monthly_payment)
      return render_template('loan.html')

# route de diabetes
@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
      prediction = None
      resultat = ''
      info = None
      dpf = ''
      # un formulaire avec asychronous request qui donne le resultat
      if request.method == 'POST':
            # get form data
            
            preg = request.form['preg']
            glucose = request.form['glucose']
            bp = request.form['bp']
            st = request.form['st']
            insulin = request.form['insulin']
            bmi = request.form['bmi']
            # conert dpf entry text to float value
            dpf = float(request.form.get('dpf'))
            print(dpf)

            age = request.form['age']
            # create array
            tab = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            # predict
            prediction = predict_diabetes(tab)
            
            if prediction[0] == 0:
                  resultat = 'NEGATIF'
                  info = 'Vous etes hors de danger, mais ne vous relachez pas. Continuez a faire du sport et a manger sainement.'
            else:
                  resultat = 'POSITIF'
                  info = 'Vous etes en danger, veuillez consulter un medecin.'
            # return prediction
      return render_template('diabetes.html', prediction=prediction, result=resultat, info=info)

# run server
if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)