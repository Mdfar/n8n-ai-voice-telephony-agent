import os from flask import Flask, request from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(name)

@app.route("/voice", methods=['GET', 'POST']) def voice(): """Respond to incoming phone calls with a TwiML voice survey""" resp = VoiceResponse()

# Start with a greeting and ask a question
gather = Gather(input='speech', action='/completed', timeout=3)
gather.say('Welcome to our AI support line. Please state the reason for your call.')
resp.append(gather)

# If the user doesn't say anything, loop back
resp.redirect('/voice')

return str(resp)


if name == "main": app.run(debug=True, port=5000)