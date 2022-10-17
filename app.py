# app.py

from flask import Flask, render_template
import os, subprocess, sys, getpass

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/adduser")
def adduser():    
    return render_template("adduser.html")

@app.route("/rmuser")
def rmuser():
    return render_template("rmuser.html")

@app.route("/eduser")
def eduser():
    return render_template("eduser.html")

def add_user():
  
     # Ask for the input
     username = input("Enter Username ")   
  
     # Asking for users password
     password = getpass.getpass()
         
     try:
         # executing useradd command using subprocess module
         subprocess.run(['useradd', '-p', password, username ])      
     except:
         print(f"Failed to add user.")                     
         sys.exit(1)

if __name__ == "__main__":
    app.run(debug=True)
