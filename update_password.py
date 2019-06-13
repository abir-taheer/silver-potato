#!/usr/bin/python3
from helpers import form
from helpers import session
import json
import hashlib

print("Content-Type: text/html\n")

if not session.is_signed_in():
	print("You are not signed in")
	exit()


users = json.loads(open("users.json").read())

if users[session.get_user_id()]["password"] != str(hashlib.sha256(form.form("old_password").encode("utf-8")).hexdigest()):
	print("Password change failed. Old password is incorrect.")
	exit()

if form.form("new_password") == form.form("verify_password") and form.form("new_password") is not None:
	users[session.get_user_id()]["password"] = str(hashlib.sha256(form.form("new_password").encode("utf-8")).hexdigest())
else:
	print("Password change failed. New passwords don't match.")
	exit()

# Save the data
open("users.json", "w").write(json.dumps(users))

print("Your updates have been stored!")
