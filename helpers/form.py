import cgi

form = {}
def update_post():
    data = cgi.FieldStorage()
    for x in data:
        form[x] = data[x].value


update_post()

