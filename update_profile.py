#!/usr/bin/python3
from helpers import form
from helpers import session
import json

print("Content-Type: text/html\n")

if not session.is_signed_in():
	print("You are not signed in! Redirecting you back in 5 seconds...")
	print('<meta http-equiv="refresh" content="5; url=./profile.py">')
	exit()


users = json.loads(open("users.json").read())

if form.form("email") is not None:
	users[session.get_user_id()]["email_address"] = form.form("email")

if form.form("preferred_name") is not None:
	users[session.get_user_id()]["preferred_name"] = form.form("preferred_name")

# Save the data
open("users.json", "w").write(json.dumps(users))

print("Your updates have been stored! Redirecting you back in 5 seconds...")
print('<meta http-equiv="refresh" content="5; url=./profile.py">')
