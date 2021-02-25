#-----------------------------------------------------------------------
# File: A1.py
# Author: Sean Elia
# Project: CMSC 447 Individual Assignment 1, Spring 2021
#
# A python file used to set up flask and react
#-----------------------------------------------------------------------

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/view')
def view():
    df = pd.read_csv("./tmp.csv")
    html = df.to_html()
    text_file = open("./Templates/table.html", "w") 
    text_file.write(html) 
    text_file.close() 
    return render_template("view.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

if __name__ == '__main__':
    app.run(debug=True)
