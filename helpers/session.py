#!/usr/bin/python3
from helpers import material
from helpers import web
from helpers import cookies
import json
import datetime


def is_signed_in():
	existing_sessions = json.loads(open("sessions.json").read())

	if cookies.get_cookie("session") is not None and cookies.get_cookie("session") in existing_sessions:
		exp = [int(x) for x in existing_sessions[cookies.get_cookie("session")]["expires"].split(",")]
		expiration_date = datetime.datetime(exp[0], exp[1], exp[2], exp[3], exp[4], exp[5])
		return expiration_date > datetime.datetime.now()
	return False

def get_user_id():
	existing_sessions = json.loads(open("sessions.json").read())
	return existing_sessions[cookies.get_cookie("session")]["username"] if is_signed_in() else None

def sign_in_card():
	return web.center_content(material.new_standard_card("This Page Requires Sign In:", "<form id='login_form' action='login.py' method='post'>" + material.new_text_input("Username", "username") + material.new_text_input("Password", "password") + "</form>", material.new_standard_button("Login", {"onclick": "document.getElementById(\"login_form\").submit()"})))

def sign_in_required():
	if not is_signed_in():
		web.add_body("<br><br>" + sign_in_card())
		web.send_content()
		exit()
