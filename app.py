import sqlite3
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

@app.route('/Home')
def Home_Page():
    # tells Flask to render the HTML page called Home.html
    return render_template('Home.html')

@app.route('/About_us')
def About_us_page():
	return render_template('About_us.html')

@app.route('/Login')
def Login_page():
	return render_template('Login.html')

@app.route('/signinform', methods=['GET', 'POST'])
def signin_form():
    if request.method == 'POST':
    	LoginID = str(request.form['LoginID'])
        Password = str(request.form['Password'])
        if LoginID in session:
            session['LoginID'] = LoginID
            return render_template('Logged in already!')
        else:
            sql = ("""Select * FROM Accounts""")
            Accounts = db.engine.execute(text(sql))
            for Account in Accounts:
                if Account['Email'] == LoginID:
                    if Account['Password'] == Password:
                        session['LoginID'] = LoginID
                        session['FullName'] = Account['firstname'] + " " + Account['lastname']
                        return 'Logged in!'   
            else:
                return "Wrong username/password!"
    else:
        return render_template('index.html')

@app.route('/signup')
def signup():
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
	app.run(host= '0.0.0.0', port=9000)