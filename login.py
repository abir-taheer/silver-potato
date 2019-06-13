#!/usr/bin/python3
from helpers import form
from helpers import session
from helpers import cookies
import json
import hashlib
import datetime
import cgitb

cgitb.enable()

print("Content-Type: text/html")

if session.is_signed_in():
	print("")
	print("You are already signed in as "+ session.get_user_id() + " !")
	exit()


users = json.loads(open("users.json").read())


if form.form("username") in users and users[form.form("username")]["password"] == str(hashlib.sha256(form.form("password").encode("utf-8")).hexdigest()):
	expires = datetime.datetime.now()
	expires = expires + datetime.timedelta(hours = 24)
	expires_string = expires.strftime("%Y,%m,%d,%H,%M,%S")

	existing_sessions = json.loads(open("sessions.json").read())

	session_token = cookies.random_str(32)

	existing_sessions[session_token] = { "username": form.form("username"), "expires": expires_string }

	open("sessions.json", "w").write(json.dumps(existing_sessions))

	print(cookies.set_cookie_str("session", session_token, expires))
	print("")

	print("Success! You are now logged in until " + expires_string + "!")

else:
	print("Error, invalid credentials")
