Summary
-
PyTwilioSimple is a Flask app to communicate with Twilio System via Webhook.  It takes a call or SMS input from the user and return the response with simple fortune from http://www.yerkee.com/api/fortune

Overall flow
User -> (call or SMS) -> Twilio -> Webhook -> Flask(localhost is exposed by ngrok) -> (Response) -> Twilio -> User

--------------------------------------------------

Environment
-
Python 3.7.6

Required packages to install:
pip install -r requirements.txt

Additional requirements

Create Twilio Account
https://www.twilio.com/

Download and install Ngrok https://ngrok.com/download

To run
- Check that your python version is 3.X
- Install the required packages
- python PyTwilioSimple.py
- Open another terminal window
- ./ngork http 5000
- After ngrok is running properly.  Copy ngrok url to twilio webhook url
(Please see attached images : 1, 2, 3)
-------------------------------------------------------------------

To use
-Simply call the twilio number or text fortune.  You will get your fortune.
