from flask import Flask, redirect, url_for, request, render_template
from flask_mail import Mail, Message
from test_selenium import *

##=======================##
## Basic Setup
##=======================##

app = Flask(__name__)
mail= Mail(app)

##=======================##
## Mail

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'temowork7@gmail.com'
app.config['MAIL_PASSWORD'] = 'zncf xkkm vgxy jxpo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

##=======================##




##=======================##
## Routes ##
##=======================##

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
     
		product = request.form['product']
		key_part = request.form['keyPart']
		data = scrape_data(product, key_part)
  
		## send mail of json file ==============
		msg = Message('Hello', sender = 'temowork7@gmail.com', recipients = ['kogantiaditya1@gmail.com'])
		msg.body = "Hello Flask message sent from Flask-Mail 2"
		with app.open_resource("output.json") as file:
			msg.attach("output.json", 'application/json', file.read())
		mail.send(msg)
  
		return "Sent: " , data
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))


if __name__ == '__main__':
	app.run(debug=True)
