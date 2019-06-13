#!/usr/bin/python3

from helpers import web
from helpers import session
from helpers import material
import json

session.sign_in_required()

grades = json.loads(open("grades.json").read())

assignments = []
for x in grades[session.get_user_id()]:
	assignments.append([x["name"], str(x["grade"]), str(x["max_points"])])
web.add_body(material.new_table(["Name", "Grade", "Max Grade"], assignments))


web.send_content()
