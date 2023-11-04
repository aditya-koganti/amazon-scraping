from flask import Flask, redirect, url_for, request, render_template
from test_selenium import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<a href="/form">go to login page?</a>'

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/form')
def formpage():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		# return redirect(url_for('success', name=user))
		data = scrape_data(user)
		return data
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))


if __name__ == '__main__':
	app.run(debug=True)
