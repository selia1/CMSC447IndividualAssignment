#-----------------------------------------------------------------------
# File: A1.py
# Author: Sean Elia
# Project: CMSC 447 Individual Assignment 1, Spring 2021
#
# A python file used to set up flask and react
#-----------------------------------------------------------------------

from flask import Flask, render_template, json
import mysql.connector
import pandas as pd

app = Flask(__name__)

def getConnection():
    # settings default, please update the formated file "config.txt" to contain the correct settings
    settings = {
        "dbName": "Students",            # Name of the databse (not table) to connect to
        "dbIP": "localhost",             # IP address for the data base
        'dbPort': 3306,                  # port number for the connection
        "dbUser": "user",                # Username for accessing the database
        "dbPass": "password",            # Password for accessing the database
    }

    # Gets default font from Config.txt
    try:
        # Reads File
        configFile = open("./config.txt", "r")

        for line in configFile:
            splitLine = (line.strip()).split(': ')
            if (splitLine[0] == "dbPort"):
                settings[splitLine[0]] = int(splitLine[1])
            else:
                settings[splitLine[0]] = splitLine[1]

        configFile.close() 

    except Exception as e:
        print(e)

    return settings

settings = getConnection()
config = {
    'user': settings["dbUser"],
    'password': settings["dbPass"],
    'host': settings["dbIP"],
    'port': settings["dbPort"],
    'database': settings["dbName"],
    'raise_on_warnings': True                    
}
#db_connection = mysql.connector.connect(**config)
#cur = db_connection.cursor()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/view')
def view():
    df = pd.read_sql("SELECT studentId AS id, studentName AS name, studentMarks AS marks FROM studentTable" , con=db_connection)
    return render_template("view.html", data = df.to_html())

@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
    return jsdata

@app.route('/edit', methods = ['POST'])
def edit():
    num = -1
    studentId = []
    studentName = []
    studentMarks = []
    if request.method == 'POST':
        stat = request.form['stat']
        idS = request.form['id']
        nmS = request.form['nm']
        mkS = request.form['mk']
        if stat:
            if stat == 0:       # Add
                if idS and nmS and mkS and int(ids) != -1:
                    cur.execute(f"INSERT INTO studentTable VALUES ({int(idS)}, {nmS}, {int(mkS)});")
                cur.execute("SELECT * FROM studentTable")
                for (idS, nameS, marksS) in cur:
                    studentId.append(idS)
                    studentName.append(nameS)
                    studentMarks.append(marksS)
            elif stat == 1:     # Update
                if idS and nmS and mkS and int(ids) != -1:
                    cur.execute(f"UPDATE studentTable SET studentName = {nmS}, studentMarks = {int(mkS)} WHERE studentId = {int(idS)};")
                cur.execute("SELECT * FROM studentTable")
                for (idS, nameS, marksS) in cur:
                    studentId.append(idS)
                    studentName.append(nameS)
                    studentMarks.append(marksS)
            elif stat == 2:     # Delete
                if idS and nmS and mkS and int(ids) != -1:
                    cur.execute(f"DELETE FROM studentTable WHERE studentId = {int(idS)};")
                    cur.execute("SELECT * FROM studentTable")
                for (idS, nameS, marksS) in cur:
                    studentId.append(idS)
                    studentName.append(nameS)
                    studentMarks.append(marksS)
            elif stat == 3:     # Select
                cur.execute("SELECT * FROM studentTable")
                for (idS, nameS, marksS) in cur:
                    studentId.append(idS)
                    studentName.append(nameS)
                    studentMarks.append(marksS)
                if idS and int(ids) != -1:
                    i = 0
                    while i < studentId.count() and studentID[i] != int(ids)
                        i += 1
                    if studentID[i] == idS
                        num = i
    else:
        cur.execute("SELECT * FROM studentTable")
        for (idS, nameS, marksS) in cur:
            studentId.append(idS)
            studentName.append(nameS)
            studentMarks.append(marksS)

    
    
    return render_template("edit.html", idS=studentId, nameS=studentName, markS=studentMarks, index = num)

if __name__ == '__main__':
    app.run(debug=True)
