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
        print(request.form.get('var_1'))
        print(request.form.get('var_2'))
        print(request.form.get('var_3'))
        print(request.form.get('var_4'))
        print(request.form.get('var_5'))
        print(request.form.get('var_6'))
        
        try:
            var_1 = float(request.form['var_1'])
            var_2 = float(request.form['var_2'])
            var_3 = float(request.form['var_3'])
            var_4 = float(request.form['var_4'])
            var_5 = float(request.form['var_5'])
            var_6 = float(request.form['var_6'])
            
            entries = [var_1, var_2, var_3, var_4, var_5, var_6]
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
            return "Please Enter valid values"

    return render_template('predict.html', prediction = model_prediction)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')