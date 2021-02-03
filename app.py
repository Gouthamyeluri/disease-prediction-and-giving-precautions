import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import json

app = Flask(__name__)
data = json.loads('data.json')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["GET",'POST'])
def predict():
    request.form.get("rate")
    request.form.get("sales in first month")
    request.form.get("sales in second month")

    #text_features = [str(x) for x in request.form.values()]
    
    in1=weights=pd.read_csv('weights.csv')
    in2=symptom_precaution = pd.read_csv('symptom_precaution.csv')
    in3=data_about = pd.read_csv('symptom_Description.csv')
    
    text_features=[]
    text_features.append(in1)
    text_features.append(in2)
    text_features.append(in3)
    
    
    text_to_int=[]
    for i in text_features:
        k=data[i]
        text_to_int.append(k)
       
    k=len(text_features)
    add_list=[]
    for i in range(0,17-k):
        add_list.append(0)
    
    final_list = text_to_int + add_list



    final_features = [np.array(final_list)]

    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)