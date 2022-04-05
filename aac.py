from flask import Flask, render_template,request
from AAC_model import model
from AAC_2 import nmodel
app=Flask(__name__)
app.config['SECRET_KEY']='432474894'


@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/coord',methods=['POST'])
def coord():
    city=request.form.get('city')
    obj=request.form.get('obj')
    print(city)
    print(obj)
    alt,az= nmodel(city,obj)
    return render_template('coord.html',alt=alt,az=az,obj=obj)

@app.route('/about')
def about():
    return render_template('about.html')