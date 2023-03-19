
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle

def build_loan_model():
    df = pd.read_csv('./datasets/loan/train.csv')

    df.dropna(subset=['LoanAmount'], inplace=True)

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.isna().sum()
    X = df.iloc[:,[8,10]].values
    y = df.iloc[:,12].values

    classifier = LogisticRegression(random_state=0)
    classifier.fit(X, y)

    test_data = pd.read_csv('./datasets/loan/test.csv')
    test_data.dropna(inplace=True)

    X_test = test_data.iloc[:,[8,10]].values

    classifier.predict(X_test)

    # nom du fichier .pkl
    filename = './models/loan.pkl'
    # export du modèle
    with open(filename, 'wb') as file:
        pickle.dump(classifier, file)

def build_diabetes_model():
    df = pd.read_csv('./datasets/diabetes/diabetes.csv')
    df.head()

    df.isna().sum()

    X = df.iloc[:,0:8].values
    y = df.iloc[:,8].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    classifier = RandomForestClassifier(n_estimators=20, random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    # write diabetes metrics (precision, Accuracy, recall, f1.score) to ./metrics.txt
    with open('./metrics.txt', 'w') as file:
        file.write("Metrics for diabetes model:")
        file.write("Accuracy: " + str(metrics.accuracy_score(y_test, y_pred)))
        file.write("Precision: " + str(metrics.precision_score(y_test, y_pred)))
        file.write("Recall: " + str(metrics.recall_score(y_test, y_pred)))
        file.write("F1 Score: " + str(metrics.f1_score(y_test, y_pred)))

    # nom du fichier .pkl
    filename = './models/diabetes.pkl'
    # export du modèle
    with open(filename, 'wb') as file:
        pickle.dump(classifier, file)

build_diabetes_model()