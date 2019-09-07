from flask import Flask, render_template
import sqlite3 as sql
import Factory

app= Flask(__name__)

def Mat():
    con = sql.connect("Data.db")
    bdguarda= con.cursor()
    query='''SELECT *
			FROM Users'''
    bdguarda.execute(query)
    return bdguarda.fetchall()

@app.route("/api/v1/users/")
def getUsers():
  return Factory.Factory().get_Api(Mat())

@app.route('/')
def index():
  return render_template('index.html', matriz = Factory.Factory().get_matriz(Mat()))


if __name__== '__main__':
    app.run(debug = True, port='3000', host='0.0.0.0')
