#!/usr/bin/python3

from helpers import web
from helpers import session
from helpers import material
from helpers import form
import json

session.sign_in_required()


# A dictionary of all of the users and their info
users = json.loads(open("users.json").read())
user_info = users[session.get_user_id()]
name = user_info["first_name"] + " " + user_info["last_name"]

web.add_body(web.center_content("<h4> Profile for " + "<b>" + str(name) + "</b> </h4>"))
web.add_body("<form action='update_profile.py' method='post'>")
web.add_body(web.center_content(material.new_text_input("Email Address", "email", user_info["email_address"], "email")))
web.add_body(web.center_content(material.new_text_input("Preferred First Name", "preferred_name", user_info["preferred_name"])))
web.add_body(web.center_content(material.new_standard_button("Save Information")))
web.add_body("</form><br><br>")


web.add_body("<form action='update_password.py' method='post' onkeyup='check_passwords()'>")
web.add_body(web.center_content(material.new_text_input("Old Password", "old_password", "", "password")))
web.add_body(web.center_content(material.new_text_input("New Password", "new_password", "", "password")))
web.add_body(web.center_content(material.new_text_input("Retype New Password", "verify_password", "", "password")))
web.add_body(web.center_content(material.new_standard_button("Change Password", {"disabled": "true", "id":"pass_change_button"})))
web.add_body("""
<script>
function check_passwords(){
	password1 = document.querySelector("input[name='new_password']");
	password2 = document.querySelector("input[name='verify_password']");
	pass_change_button = document.getElementById("pass_change_button");
	if( password1.value === password2.value && password1.value !== "" ){
		pass_change_button.removeAttribute("disabled");
	} else {
		pass_change_button.setAttribute("disabled", true);
	}
}
</script>
""")
web.add_body("</form><br>")
web.send_content()
