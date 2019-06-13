#!/usr/bin/python3
import os
import random
from datetime import datetime as datetime
from urllib.parse import unquote_plus as uri_decode
from urllib.parse import quote as uri_encode


cookie_cache = None

def setup_cookies():
    global cookie_cache
    if cookie_cache is None:
        cookie_cache = {}
        if "HTTP_COOKIE" in os.environ:
            # Parse the cookies to see what the browser sent
            for x in os.environ["HTTP_COOKIE"].split("; "):
                equal_loc = x.find("=")
                cookie_cache[uri_decode(x[:equal_loc])] =  uri_decode(x[equal_loc + 1:])

setup_cookies()

def get_cookie(name):
    global cookie_cache
    return cookie_cache[name] if name in cookie_cache else None


def set_cookie_str(name, value = "", expiration = None, path = None, domain = None, https = None, httponly = None):
    cookie_str = "Set-Cookie: " + uri_encode(name) + "=" + uri_encode(value) + ";"
    if expiration is not None:
        cookie_str += " expires=" + expiration.strftime("%a, %d %b %Y %H:%M:%S") + ";"
    if path is not None:
        cookie_str += " path=" + uri_encode(path) + ";"
    if domain is not None:
        cookie_str += " domain=" + domain + ";"
    if https:
        cookie_str += " secure;"
    if httponly:
        cookie_str += " httponly;"
    return cookie_str


def random_str(length, lowercase_letters = True, uppercase_letters = False, numbers = True):
	allowed = ""
	str = ""

	if lowercase_letters:
		allowed += "abcdefghijklmnopqrstuvwxyz"

	if uppercase_letters:
		allowed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if numbers:
		allowed += "1234567890"

	for x in range(length):
		str += allowed[random.randrange(len(allowed))]

	return str
