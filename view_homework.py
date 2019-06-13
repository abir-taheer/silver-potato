#!/usr/bin/python3

from helpers import web
from helpers import session

session.sign_in_required()

web.add_body("This is p cool")

web.send_content()
