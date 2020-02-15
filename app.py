from flask import Flask, session, redirect, url_for, escape, request, render_template, g

app=Flask(__name__)

@app.route('/')
@app.route('/Home')
def root():
    # tells Flask to render the HTML page called Home.html
    return render_template('Home.html')

@app.route('/About_us')
def About_us_page():
	return render_template('About_us.html')

@app.route('/Login')
def Login_page():
	return render_template('Login.html')

@app.route('/Admin_login')
def Admin_login_page():
	return render_template('Admin_login.html')

if __name__ == '__main__':
	app.run(host= '0.0.0.0', port=9000)