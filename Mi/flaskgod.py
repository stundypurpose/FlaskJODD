#!/bin/python

from flask import Flask, render_template
import requests
import json

app  = Flask(__name__)

#def get_api():

@app.route("/")
#def first():
#	return "HIRE ME BITCH OR I'LL BANKRUPT DATAVIZZ"
	
def index():
	return render_template("date_index.html")

app.run(host="0.0.0.0" , port= 80)
