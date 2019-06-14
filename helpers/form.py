import cgi

form_fields = {}
data = cgi.FieldStorage()
def update_post():
    global data
    for x in data:
        form_fields[x] = data[x].value


update_post()

def form(key):
	return form_fields[key] if key in form_fields else None
