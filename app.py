import sqlite3
import requests
from flask import Flask, session, redirect, url_for, escape, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app=Flask(__name__)
app.secret_key = 'George#1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///camApp.db'
db = SQLAlchemy(app)

@app.route('/')
def root():
	return render_template('Home.html')

@app.route('/Home.html')
def Home_Page():
    # tells Flask to render the HTML page called Home.html
    return render_template('Home.html')

@app.route('/About_us.html')
def About_us_page():
	return render_template('About_us.html')

@app.route('/Contact_us.html')
def Contact_us_page():
	return render_template('Contact_us.html')

@app.route('/Acc_info.html')
def Acc_info_page():
	return render_template('Acc_info.html')

@app.route('/Login.html')
def Login_page():
	return render_template('Login.html')

@app.route('/signinform', methods=['GET', 'POST'])
def signin_form():
    if request.method == 'POST':
        LoginID = str(request.form['LoginID'])
        Password = str(request.form['Password'])
        if LoginID in session:
            session['LoginID'] = LoginID
            flash('You are already logged in')
            return render_template('UserInterface')
        else:
            sql = ("""Select * FROM Accounts""")
            Accounts = db.engine.execute(text(sql))
            for Account in Accounts:
                if Account['Email'] == LoginID:
                    if Account['Password'] == Password:
                        session['LoginID'] = LoginID
                        session['FullName'] = Account['firstname'] + " " + Account['lastname']
                        return render_template('UserInterface.html')   
            else:
                flash('Wrong username/password!')
                return render_template('Login.html')
    else:
        return render_template('index.html')

@app.route('/trustedvisitor', methods=['GET', 'POST'])
def trusted_visitor():
    if request.method == 'GET' or request.method == 'POST':
        return render_template('Trusted_visitor.html')
    return "<h1>OOPS!</h1>" 

@app.route('/unknownvisitor', methods=['GET', 'POST'])
def unknown_visitor():
    if request.method == 'GET' or request.method == 'POST':
        return render_template('Unknown_visitor.html')
    return "<h1>OOPS!</h1>" 

@app.route("/signup.html")
def signup_page():
    return render_template('signup.html')

@app.route('/signupform', methods=['GET', 'POST'])
def signup_form():
    if request.method == 'POST':
        firstname = str(request.form['firstname'])
        lastname = str(request.form['lastname'])
        LoginID = str(request.form['emailadd'])
        Password = str(request.form['password'])
        sql = ("""INSERT INTO Accounts VALUES ('{}', '{}', '{}', '{}')""".format(firstname, lastname, LoginID, Password))
        db.engine.execute(text(sql))
        return "Signin Recorded!!!"
    else:
        return "Signup not recorded!!!"

if __name__ == '__main__':
	app.run(host= '127.0.0.1')