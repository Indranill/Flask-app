from flask import Flask, render_template, request, redirect 
from werkzeug.utils import secure_filename
import os
import pandas as pd
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/data',methods=['GET','POST'])
def data():
    f_row="no files found"
    if request.method=='POST':
        file = request.files['xlfile']
        if file:
            d=pd.read_excel(file)
            d.iloc[:,0]
            d=d.to_json()

    return render_template('data.html', data = d)

if __name__ == '__main__':
    app.run(debug=True)