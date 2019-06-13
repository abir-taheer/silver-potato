#!/usr/bin/python3

from helpers import web
from helpers import session

session.sign_in_required()


web.send_content()
# Use the session.get_user_id() function to get the user's username and then their relevant information
