from email_validator import validate_email as validator
from flask import Flask, escape, jsonify, request
from flask_cors import CORS

import sqlite3
import requests

CAPTCHA_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

app = Flask(__name__)

def validate_email(email):
    try:
        validator(email)
        return True
    except Exception:
        return False

def validate_captcha(captcha: str):
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', params={"secret" : CAPTCHA_KEY,"response" : captcha })
    return r.json()['success']

def add_email(email):
    con = sqlite3.connect('email.db')
    con.cursor().execute("INSERT INTO email VALUES (?)", (email,))
    con.commit()
    con.close()
    return True

@app.route("/", methods=["POST"])
def email():
    email = escape(request.form['email'])
    captcha = escape(request.form['captcha'])

    if validate_email(email) and validate_captcha(captcha):
        try:
            return jsonify({"success": add_email(email)})
        except:
            return jsonify({"success": False})
    return jsonify({"success": False})

