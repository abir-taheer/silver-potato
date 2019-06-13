#!/usr/bin/python3
from helpers import material
from helpers import web
def is_signed_in():
    return False

def get_user_id():
    return "kmisquitta10"

def sign_in_card():
	return web.center_content(material.new_standard_card("This Page Requires Sign In:", material.new_text_input("Username", "username") + material.new_text_input("Password", "password"), material.new_standard_button("hey")))

def sign_in_required():
	if not is_signed_in():
		web.add_body("<br><br>" + sign_in_card())
		web.send_content()
		exit()
