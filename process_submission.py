#!/usr/bin/python3
from helpers import session
from helpers import form
import json
import cgi

print("Content-Type: text/html")
print("")
file_data = form.data['homework_file'].file.read()
