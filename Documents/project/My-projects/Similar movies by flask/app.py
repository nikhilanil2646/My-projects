from flask import Flask,render_template,request
import pymysql as sql
import pymysql.cursors 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return "nik here"
  
@app.route("/backend/",methods=['GET','POST'])
def backend():
    if request.method == "POST":
       movie =request.form.get("m_name")
      
              
       import sys
       sys.path.insert(0, '/')
       import mr
       simtemp=mr.mr.mrf(movie)
       movie1=movie.replace(" ","")
       return render_template("backend.html",movie1=movie,arr=simtemp,url=f"/static/{movie1}.png")

@app.route("/temp/<var>/",methods=['GET','POST'])
@app.route("/temp/",methods=['GET','POST'])
def temp(var=None):
       r=['m','mo_name']
       movies = pd.read_csv(os.path.join("C:/Users/nikhi/Desktop/btch1pm/MachineLearning/knn/ml-100k/u.item"),index_col='m', sep='|',names=r,usecols=range(2),encoding="ISO-8859-1")
       movies=pd.DataFrame(movies)
       if request.method == "POST":
              var =request.form.get("m_name")
       mo=var
       mo=mo.capitalize()
       msl=list(movies['mo_name'])
       if var in msl:
              import sys
              sys.path.insert(0, '/')
              import mr
              simtemp=mr.mr.mrf(var)
              movie1=var.replace(" ","")
              return render_template("backend.html",movie1=var,arr=simtemp,url=f"/static/{movie1}.png")
       
       data=pd.DataFrame()
       data["ind"]= movies['mo_name'].str.find(mo)
       movlist=list()
       for i in range(1,len(movies)):
           if data['ind'][i]==0:
              print(movies['mo_name'][i])
              movlist.append(movies['mo_name'][i]) 
       return render_template("temp.html",vr=mo,movie1=movlist)




app.run(host="localhost",debug=True)  
