# # # The program is used to to predict diabetes occurance.

# # # Copyright (C) 2022  Syed Salman Habeeb Quadri

# # # This program is free software: you can redistribute it and/or modify
# # # it under the terms of the GNU General Public License as published by
# # # the Free Software Foundation, either version 3 of the License, or
# # # (at your option) any later version.

# # # This program is distributed in the hope that it will be useful,
# # # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# # # GNU General Public License for more details.

# # # The GNU General Public License does not permit incorporating this program
# # # into proprietary programs.

# # # You should have received a copy of the GNU General Public License
# # # along with this program.  
# # # If not, see [GNU General Public License](https://www.gnu.org/licenses/).

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
