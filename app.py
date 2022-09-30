from flask import Flask, render_template,request
from mydb import connect
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("indexx.html")

@app.route("/loginpage", methods=['POST']) 
def result():
    email = request.form['email']
    uname = request.form['uname']
    rollno = request.form['rollno']
    Pass = request.form['Pass'] 
    
    connect.insert_values(email,uname,rollno,Pass)
    return "Data received! Thank you {}".format(uname)
    

if __name__ == "__main__":
    app.run(debug=True)


    