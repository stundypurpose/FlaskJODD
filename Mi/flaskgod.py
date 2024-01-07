#!/bin/python

from flask import Flask, render_template, request
import requests
import json
import sqlalchemy
import dask.dataframe as dd

app  = Flask(__name__)

#def get_api():

@app.route("/")
#def first():
#	return "HIRE ME BITCH OR I'LL BANKRUPT DATAVIZZ"
	
def index():
	return render_template("date_index.html")
	
@app.route('/', methods=['POST'])
def getvalue():
	startdate = request.form['startdate']
	enddate = request.form['enddate']
	return render_template('pass.html', s=startdate , e=enddate)

@app.route('/')
def dask():
#	ddf=dd.read_sql('test_table1',r"mysql://root:root@localhost:3001/test_db","Lat")
#	return render_template(you desire data)
#print(ddf.tail())

app.run(host="0.0.0.0" , port= 80)
