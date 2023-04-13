# import main flask librairies
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pickle as pkl
import os, pandas as pd
from sklearn.preprocessing import LabelEncoder
# Diabetes model
file_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'diabetes.pkl')

with open(file_path, 'rb') as f:
      diabetes_model = pkl.load(f)

# Churn model 
file_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'churn_xgb_model.pkl')

with open(file_path, 'rb') as f:
      xgb = pkl.load(f)


# init app
app = Flask(__name__)

###############################################
# PROCESSING
###############################################
def predict_diabetes(tab):
      pred = diabetes_model.predict(tab)
      return pred

def encode_Categorical_features(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
    return df

def predict_new_data(Xnew):
      # si c'est un dictionnaire on le transforme en dataframe
      if type(Xnew) == dict:
            Xnew = pd.DataFrame(Xnew, index = [0])
      Xnew = encode_Categorical_features(Xnew)
      return xgb.predict(Xnew)

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
            pass
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

# route de churn
import json
@app.route('/churn', methods=['GET', 'POST'])
def churn():
    """
    churn prediction : 
    this route is used to predict if a customer will churn or not
    une entree ressemble a {'CreditScore': 600, 'Geography':'Spain', 'Gender':'Female', 'Age': 40, 'Tenure': 3, 'Balance': 60000, 'NumOfProducts': 2, 'HasCrCard': 1, 'IsActiveMember': 1, 'EstimatedSalary': 50000} 
    definissons une route qui recuperes les champs du formulaire et les convertis en json pour les envoyer au modele de prediction
    """
    predict = []
    if request.method == 'POST':
        # récupération des données du formulaire
        CreditScore = int(request.form.get('CreditScore'))
        Geography = request.form.get('Geography')
        Gender = request.form.get('Gender')
        Age = int(request.form.get('Age'))
        Tenure = int(request.form.get('Tenure'))
        Balance = int(request.form.get('Balance'))
        NumOfProducts = int(request.form.get('NumOfProducts'))
        HasCrCard = int(request.form.get('HasCrCard'))
        IsActiveMember = int(request.form.get('IsActiveMember'))
        EstimatedSalary = int(request.form.get('EstimatedSalary'))

        # transformation des données en un dictionnaire JSON
        input_data = {
            'CreditScore': CreditScore,
            'Geography': Geography,
            'Gender': Gender,
            'Age': Age,
            'Tenure': Tenure,
            'Balance': Balance,
            'NumOfProducts': NumOfProducts,
            'HasCrCard': HasCrCard,
            'IsActiveMember': IsActiveMember,
            'EstimatedSalary': EstimatedSalary
        }
        input_data_json = json.dumps(input_data)

        print(input_data)
        

        # utilisation du modèle pour faire la prédiction
        predict = predict_new_data(input_data)
        predict = predict[0]
        print("predict=",predict)
    # retourne le template HTML avec le résultat de la prédiction
    return render_template('churn.html', predict=predict)


if __name__ == '__main__':
      app.run(debug=True, port=5000, host='0.0.0.0')
