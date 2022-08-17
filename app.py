from email import message
import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request

app=Flask(__name__, template_folder = "assets/templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    
    if request.method == 'POST':
        print(request.form.get('no_of_pregnancies'))
        print(request.form.get('glucose_level'))
        print(request.form.get('insulin'))
        print(request.form.get('bmi'))
        print(request.form.get('dpf'))
        print(request.form.get('age'))
        
        try:
            no_of_pregnancies = float(request.form['no_of_pregnancies'])
            glucose_level = float(request.form['glucose_level'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = float(request.form['age'])
            
            insulin = np.log1p(insulin)
            
            entries = [no_of_pregnancies, glucose_level, insulin, bmi, dpf, age]
            entries = np.array(entries)
            scaling_df = pd.read_csv("assets/scaling_data.csv")
            for i, entry in enumerate(entries):
                entries[i] = (entry - scaling_df.iloc[0, i + 1])/scaling_df.iloc[1, i + 1]
            entries = entries.reshape(1, -1)
            with open("assets/model.dat", "rb") as f:
                lr_model = pickle.load(f)
            model_prediction = lr_model.predict(entries)[0]
            if model_prediction == 1.0:
                model_prediction = "Positive (+ve)"
            else:
                model_prediction = "Negative (-ve)"

        except ValueError:
            return render_template('index.html', message = "Please enter numeric values only")

    return render_template('predict.html', prediction = model_prediction)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')