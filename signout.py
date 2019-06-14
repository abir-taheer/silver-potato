#!/usr/bin/python3
from helpers import cookies
import datetime

print("Content-Type: text/html")
print(cookies.set_cookie_str("session", "", (datetime.datetime.now() - datetime.timedelta(hours = 8760))))
print("")
print("You have been successfully signed out! Redirecting you back in 5 seconds...")
print('<meta http-equiv="refresh" content="5; url=./profile.py">')
