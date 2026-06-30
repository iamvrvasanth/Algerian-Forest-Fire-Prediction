import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
from flask import Flask,render_template,request,jsonify

application = Flask(__name__)
app=application

# loading the ridge and scaler model file


ridge=pickle.load(open('models/ridge.pkl','rb'))
scaler=pickle.load(open('models/scaler.pkl','rb'))

#home page this is 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == "POST":

        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data = scaler.transform([[Temperature, RH, Ws, Rain,
                                      FFMC, DMC, ISI, Classes, Region]])

        result = ridge.predict(new_data)

        return render_template("form.html", results=round(result[0], 2))

    else:
        return render_template("form.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)