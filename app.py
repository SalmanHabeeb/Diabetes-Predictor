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
        try:
            no_of_pregnancies = float(request.form['no_of_pregnancies'])
            glucose_level = float(request.form['glucose_level'])
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            age = float(request.form['age'])
            
            bmi = weight/(height/100)**2
            
            entries = [no_of_pregnancies, glucose_level, bmi, age]
            entries = np.array(entries)
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