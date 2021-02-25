#-----------------------------------------------------------------------
# File: A1.py
# Author: Sean Elia
# Project: CMSC 447 Individual Assignment 1, Spring 2021
#
# A python file used to set up flask and react
#-----------------------------------------------------------------------

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/view')
def view():
    return render_template("view.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

if __name__ == '__main__':
    app.run(debug=True)
