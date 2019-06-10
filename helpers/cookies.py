#!/usr/bin/python3
print("Content-Type: text/html")
print("")

import os
from datetime import datetime as datetime
from urllib.parse import unquote_plus as uri_decode
from urllib.parse import quote as uri_encode

for x in os.environ:
    print(x, os.environ[x])

cookie_cache = None
def get_cookies():
    if cookie_cache is None:
        cookie_cache = {}
        if "HTTP_COOKIE" in os.environ:
            # Parse the cookies to see what the browser sent
            for x in os.environ["HTTP_COOKIE"].split("; "):
                equal_loc = x.find("=")
                cookie_cache[uri_decode(x[:equal_loc])] =  uri_decode(x[equal_loc + 1:])
    return cookie_cache


def get_cookie(name):
    if name in get_cookies():
        return get_cookies[name]
    return None


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


print(get_cookies())
