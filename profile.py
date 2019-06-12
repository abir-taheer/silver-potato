#!/usr/bin/python3

from helpers import web

web.add_http_header("Content-Type", "text/html")
web.add_body("This is p cool")

web.send_content()
