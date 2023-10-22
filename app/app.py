from flask import Flask, render_template, request
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
from joblib import load
import os

def convert_(x):
    try:
        float(x)
        return float(x)
    except:
        return -1

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        academic_qualification = request.form['academic-qualification']
        model, d = load(f"./app/music-recommender.joblib")
        dic = {d[0][i]:{a:b for a,b in zip(d[1][i][0],d[1][i][1])} for i in range(len(d[0]))}
        predictions = model.predict([[dic.get(i_,{x_:convert_(x_)}).get(x_, -1) for i_,x_ in enumerate([myage, mygender, academic_qualification])]])
        return render_template('index.html', href2='The suitable music for you (age:'+str(myage)+' ,gender:'+str(mygender)+',academic qualification:'+str(academic_qualification)+') is:'+ str(predictions[0]))

