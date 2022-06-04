from flask import Flask,jsonify
import joblib
import pandas as pd
from flask import request
#CREATE FLASK APP THEN CONNECT POST API CALL
app=Flask(__name__)
#LOAD MY MODEL and LOAD COLUMN NAMES
@app.route('/predict',methods=['POST'])
def predict():
    feat_data=request.json
    df=pd.DataFrame(feat_data)
    df=df.reindex(columns=col_names)
    prediction=list(model.predict(df))
    return jsonify({'prediction':str(prediction)})

if__name__ =='__main__':
    model=joblib.load("week4_model.pkl")
    col_names=joblib.load("col_names.pkl")
    app.run(debug=True)
    
    