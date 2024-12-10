from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/home", methods = ["GET"])
def frontend():
    return render_template("index.html")

database=[]
@app.route("/reg_data", methods = ["POST"])
def get_reg_data():
    user={}
    name=request.form["uname"]
    email=request.form["uemail"]
    phonenumber=request.form["uph"]
    Password=request.form["upswd"]
    user["user_name"]=name
    user["user_email"]=email
    user["user_phn"]=phonenumber
    user["user_password"]=Password
    #return [name,email,phonenumber,Password]
    database.append(user)
    return redirect("/home")

@app.route("/login_data",methods=["POST"]) 
def get_login_data():
    email=request.form["uemail"] 
    Password=request.form["upswd"] 
    for user in range(len(database)):
        log_email=database[user]["user_email"] 
        log_pswd=database[user]["user_password"]
        if email==log_email and Password==log_pswd:
            return "Login Successful :) "
        else:
            return "Invalid Login Credentials :("
    #return (email,Password)

app.run(debug=True)
