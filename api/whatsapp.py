from twilio.rest import Client
from flask import Flask 
import os

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello, World!' 

@app.route('/msg/<string:msg>')
def reply(msg):
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=msg,
  to='whatsapp:+917291918201'
  )
  print(message.sid)
  return "Message has been sent successfully"

    
if __name__ == "__main__":
    app.run(debug=True)
