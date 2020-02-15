from flask import Flask, session, redirect, url_for, escape, request, render_template, g

app=Flask(__name__)

@app.route('/')
def root():
    # tells Flask to render the HTML page called Home.html
    return render_template('Home.html')

@app.route('/About_us')
	return render_template('About_us.html')

@app.route('/Home')
	return render_template('Home.html')

@app.route('/Login')
	return render_template('Login.html')

@app.route('/Admin_login')
	return render_template('Admin_login.html')

if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0', port=9000)