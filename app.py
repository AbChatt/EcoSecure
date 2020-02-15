from flask import Flask, session, redirect, url_for, escape, request, render_template, g

app=Flask(__name__)

@app.route('/')
def root():
    # tells Flask to render the HTML page called index.html
    return render_template('Home.html')


if __name__ == '__main__':
	app.run(host= '0.0.0.0', port=9000)