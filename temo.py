from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'temowork7@gmail.com'
app.config['MAIL_PASSWORD'] = 'zncf xkkm vgxy jxpo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'temowork7@gmail.com', recipients = ['kogantiaditya1@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail 2"
   with app.open_resource("output.json") as file :
       msg.attach("output.json", 'application/json', file.read())
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)