# # # This file is part of Diabetes-Predictor.

# # # Diabetes-Predictor is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# # # Diabetes-Predictor is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# # # You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>.


import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
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
            scaling_df = pd.read_csv("assets/scaling_data.csv")
            for i, entry in enumerate(entries):
                entries[i] = (entry - scaling_df.iloc[0, i + 1])/scaling_df.iloc[1, i + 1]
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
            return "Please Enter valid values"

    return render_template('predict.html', prediction = model_prediction)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
