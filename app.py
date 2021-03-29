
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('heart_Failure_Prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        anaemia=request.form['anaemia']
        hbp=request.form['hbp']
        serium_sodium = int(request.form['serium_sodium'])
        ef = int(request.form['ef'])
        time = int(request.form['time'])
        
        if age>70:
            senior_citizen = 1
        else:
            senior_citizen = 0
            
        if time>70:
            less_time = 0
        else:
            less_time = 1
            
        if anaemia == 'Yes':
            anaemia = 1
        else:
            anaemia = 0
            
        if hbp == 'Yes':
            hbp = 1
        else:
            hbp = 0
            
        if serium_sodium < 134:
            low_serum_sodium = 1
        else:
            low_serum_sodium = 0
            
        if ef < 32:
            low_ejection_fraction = 1
        else:
            low_ejection_fraction = 0
        
        prediction=model.predict([[senior_citizen, less_time, low_serum_sodium, low_ejection_fraction, anaemia, high_blood_pressure]])
        
        if int(prediction)==1:
            return render_template('index.html',prediction_text="You are vulnerable to heart failure. Please take good care of yourself!!")
        else:
            return render_template('index.html',prediction_text="You are safe from heart failure. Enjoy!!")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)