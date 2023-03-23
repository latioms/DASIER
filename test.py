
import pickle as pkl


# load the model diabetes from models 
with open('models/diabetes.pkl', 'rb') as f:
    model = pkl.load(f)

# try to predict  wit a new data

# new data
new_data = [[6,148,72,35,0,33.6,0.627,50]]

# predict WITH the confidence
pred = model.predict(new_data)

# print the prediction
print('Prediction: ', pred, 'Confidence: ', model.predict_proba(new_data))

print(pred)