# import main flask librairies
from flask import Flask, render_template, request, redirect, url_for, flash

import os

# init app
app = Flask(__name__)

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
      if request.method == 'POST':
            # get form data
            pregnancies = request.form['pregnancies']
            glucose = request.form['glucose']
            blood_pressure = request.form['blood_pressure']
            skin_thickness = request.form['skin_thickness']
            insulin = request.form['insulin']
            bmi = request.form['bmi']
            diabetes_pedigree_function = request.form['diabetes_pedigree_function']
            age = request.form['age']
            # format diabetes to 2 decimal places
            diabetes = "{:.2f}".format(diabetes)
            # return diabetes
            return render_template('diabetes.html', diabetes=diabetes)


# run server
if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)