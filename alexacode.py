from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
from getsentiment import getInvestorSentiment

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    welcome_message = "Do you want to know today's investor sentiment?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_investor():
    sentiment_msg = getInvestorSentiment()
    return statement(sentiment_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "Okay... bye!"
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=False)
