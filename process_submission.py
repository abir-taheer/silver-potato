#!/usr/bin/python3
from helpers import session
from helpers import cookies
from helpers import form
import json
import cgi
import os
import datetime

print("Content-Type: text/html")

def simple_message(message):
	print("")
	print(message)
	print("<br>")
	print('Redirecting you back in 5 seconds...<meta http-equiv="refresh" content="5; url=./profile.py">')
	exit()

if not session.is_signed_in():
	simple_message("You need to be signed in to use this feature!")


existing_homeworks= json.loads(open("homeworks.json").read())

homework_id = form.form("homework_id")

if homework_id not in existing_homeworks:
	simple_message("That homework does not exist!")


homework_submissions = json.loads(open("submissions.json").read())

if homework_id in homework_submissions[session.get_user_id()]:
	os.remove("submissions/" + homework_submissions[session.get_user_id()][homework_id]["filename"])


new_filename = homework_id + "-" + session.get_user_id() +  "-" + cookies.random_str(6) + ".txt"
comments = form.form("comments")


homework_submissions[session.get_user_id()][homework_id] = {
	"filename": new_filename,
	"time": datetime.datetime.now().strftime("%Y,%m,%d,%H,%M,%S"),
	"comments": comments
}

file_data = form.data['homework_file'].file.read()

open("submissions.json", "w").write(json.dumps(homework_submissions))

open("submissions/" + new_filename, "w+").write(str(file_data))

simple_message("Homework sucessfully uploaded!")
