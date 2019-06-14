#!/usr/bin/python3

from helpers import web
from helpers import session
from helpers import material
import json



session.sign_in_required()

data = []

all_homeworks = json.loads(open("homeworks.json", "r").read())
my_submissions = json.loads(open("submissions.json", "r").read())[session.get_user_id()]

for homework_id in all_homeworks:
	this_row = [all_homeworks[homework_id]["name"]]
	if homework_id in my_submissions:
		this_row.append("<a href='submissions/" + my_submissions[homework_id]["filename"] + "' target='_blank'>View Submission</a>")
		this_row.append(str(my_submissions[homework_id]["comments"]))
	else:
		this_row.append("No Submission")
		this_row.append("N/A")
	data.append(this_row)

web.add_body("<br><br>" + web.center_content(material.new_table(["Name", "Submission", "Comments"], data)))

web.send_content()
