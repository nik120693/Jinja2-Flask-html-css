# app.py

from crypt import methods
from flask import Flask, render_template, request
import os, subprocess, sys, getpass

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/adduser")
def adduser():    
    return render_template("adduser.html")

@app.route("/adduser", methods=['POST'])
def add_user():
  
     # Ask for the input
     username = request.form['username']
     print(username)   
  
     # Asking for users password
     password = request.form['password']
     print(password)    
     try:
         # executing useradd command using subprocess module
         subprocess.run(['useradd', '-p', password, username ])
         return home()    
     except:
         print(f"Failed to add user.")                     
         sys.exit(1)

@app.route("/rmuser")
def rmuser():
    return render_template("rmuser.html")

@app.route("/rmuser", methods=['POST'])
def removeUser():
    name = request.form['name']
    os.system("sudo deluser --remove-home "+name)
    print("User deleted")
    
@app.route("/eduser")
def eduser():
    return render_template("eduser.html")



if __name__ == "__main__":
    app.run(port=8000, debug=True)
