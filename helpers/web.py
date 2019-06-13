#!/usr/bin/python3

template = open("template.txt").read()
body = ""
head = ""
http_headers = "Content-Type: text/html\n"


def add_body(content):
	global body
	body += content


def add_http_header(header, value):
	global http_headers
	http_headers += header + ": " + value + "\n"


def send_content():
	global http_headers
	global template
	global body
	global head
	print(http_headers)
	print(template.replace("<!--Head_Content-->", head).replace("<!--Body_Content-->", body))

def center_content(content):
	return "<div class='ctr-obj'>" + content + "</div>"
