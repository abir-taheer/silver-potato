import cgi

form_fields = {}
def update_post():
    data = cgi.FieldStorage()
    for x in data:
        form_fields[x] = data[x].value


update_post()

def form(key):
	return form_fields[key] if key in form_fields else None
