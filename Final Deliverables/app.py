from flask import Flask ,render_template, request, redirect
import dbconn
import ibm_db
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("reg.html")

@app.route("/home")
def home():
    return render_template("homef.html")
 
#registration page code


@app.route("/signup", methods=['POST'])
def signup():
       if request.method == 'POST':
         email = request.form.get('email')
         uname = request.form.get('uname')
         Pass = request.form.get('Pass')
         sql = "INSERT INTO STUDENT_DB (email,USERNAME, PASSWORD) VALUES ('{0}','{1}','{2}')"
         res = ibm_db.exec_immediate(dbconn.conn, sql.format( email,uname, Pass))
         if sql:
            return redirect("/home")
         else:
            return redirect("/")
       else:
        print("Could'nt store anything...")



if __name__ == "__main__":
    app.run(debug=True)