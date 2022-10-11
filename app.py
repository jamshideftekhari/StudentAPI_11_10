from flask import Flask, url_for, render_template, redirect, request
from datetime import datetime
import random
from Controller import Controller


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> hello, world </p> "

@app.route("/Time/")
def Time():
    return "<h1> current time is: " + str(datetime.now()) +" </h1> <br> <h1> Random number generated:  " + str(random.randint(1,11))+ "</h1>"

@app.route("/students")
def Students():
    mycontroller = Controller()
    #students = mycontroller.ReadData()
    return render_template("students.html", students = mycontroller.ReadData())

@app.route("/AddStudent", methods=['POST'])
def AddStudent():
    mycontroller = Controller()
    print(request.form['fname'], request.form['lname'])
    mycontroller.CreateData(request.form['fname'], request.form['lname'])
    return redirect(url_for('Students'))

#app.run()
app.run('0.0.0.0', port=5000, debug=True)