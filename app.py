import sqlite3
from flask import Flask, session, redirect, url_for, escape, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app=Flask(__name__)
app.secret_key = 'George#1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment3.db'
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
            return render_template('Lecture.html')


@app.route('/Admin_login')
def Admin_login_page():
	return render_template('Admin_login.html')

if __name__ == '__main__':
	app.run(host= '0.0.0.0', port=9000)