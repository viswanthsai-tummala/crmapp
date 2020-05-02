from flask import render_template,Flask,request
import datetime
from database import EmployeeDataBase

app = Flask(__name__)
db = EmployeeDataBase('./data/db.json')

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html", currenttime=datetime.datetime.now())

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        empid = request.form["employeeid"]
        name , activecases = db.activebacklog(str(empid))
        return render_template("result.html", employeedetails= [name, empid, activecases], currenttime=datetime.datetime.now())


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)