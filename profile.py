#!/usr/bin/python3

from helpers import web
from helpers import session
from helpers import material
from helpers import form
import json


# A dictionary of all of the users and their info
users = json.loads(open("users.json").read())
user_info = users[session.get_user_id()]
name = user_info["first_name"] + " " + user_info["last_name"]

# session.sign_in_required()
web.add_body('<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700" type="text/css">')

web.add_body(web.center_content("<h4> Profile for " + "<b>" + str(name) + "</b> </h4>"))
web.add_body(web.center_content(material.new_text_input("Email Address", user_info["email_address"])))
web.add_body(web.center_content(material.new_text_input("Preferred First Name", user_info["first_name"])))
web.add_body(web.center_content(material.new_text_input("New Password", "")))
web.add_body(web.center_content(material.new_text_input("Retype New Password", "")))

web.send_content()
