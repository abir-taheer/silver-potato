#!/usr/bin/python3

from helpers import web
from helpers import session
from helpers import material
import json
session.sign_in_required()

homework_select =  '<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label"><select class="mdl-textfield__input" name="homework_id">'

homeworks = json.loads(open("homeworks.json").read())

for homework in reversed(homeworks):
	homework_select += '<option value="'+ homework["id"] +'">'+ str(homework["name"]) +'</option>'

homework_select += '</select><label class="mdl-textfield__label">Homework</label></div>'

web.add_body("<br><br><form action='process_submission.py' method='post' enctype='multipart/form-data'>" + web.center_content(
material.new_standard_card("Submit Homework",
homework_select +
"<input type='file' name='homework_file'>" +
"""
<div class="mdl-textfield mdl-js-textfield">
    <textarea class="mdl-textfield__input" type="text" rows= "3" cols='5' name='comments'></textarea>
    <label class="mdl-textfield__label">Comments...</label>
  </div>
"""
, material.new_standard_button("Submit") )) + "</form>")

web.send_content()
# Use the session.get_user_id() function to get the user's username and then their relevant information
