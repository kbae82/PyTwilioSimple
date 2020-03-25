from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import urllib, json
import requests
import re
import os

app = Flask(__name__)


@app.route("/voice", methods=['POST'])
def voice():
    #Respond to incoming phone calls with a brief message.
    # Start TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    message = "Welcome to the Fortune teller line, Here is your fortune."
    resp.say(message, voice='alice')
    resp.pause(length=1)
    message2 = get_fortune() + ".  Thank you, have a great day!"
    resp.say(message2, voice='alice')
    return str(resp)

@app.route("/sms_reply", methods=['GET', 'POST'])
def sms_reply():
    #Respond to incoming calls with a simple text message.
    #Start TwiML response
    resp = MessagingResponse()
    body = request.form['Body']
    if "fortune" in body.lower().strip():
        # GET fortune
        resp.message("=====\n\nHello there, your Fortune says, " + get_fortune()+"\"")
    else:
        resp.message("=====\n\nSorry, do you want to know your fortune? please type 'Fortune'")
    return str(resp)


def get_fortune():
    # REST API CALL to the fortune API
    fortune_REST_info = requests.get("http://www.yerkee.com/api/fortune")
    json_info = json.loads(fortune_REST_info.text)
    result_data = json_info['fortune']
    return result_data

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
