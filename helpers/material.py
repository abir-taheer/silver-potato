#!/usr/bin/python3

def new_standard_button(text, classes = ["mdl-button--raised", "mdl-button--colored", "mdl-js-ripple-effect"], attributes = {}):
	button = "<button class='mdl-button mdl-js-button "+ " ".join(classes) +"' "
	for attr in attributes:
		button += str(attr) + "='" + attributes[attr] + "' "
	button += ">" + text + "</button>"
	return button


def new_standard_card(title =None, content = None, bottom = None):
	card =  '<div class="mdl-card mdl-shadow--2dp">'
	if title is not None:
		card += """
		<div class="mdl-card__title">
  	    	<h2 class="mdl-card__title-text">""" + title +"""</h2>
  	  	</div>
	  	"""
	if content is not None:
		card += """
		<div class="mdl-card__supporting-text">
  	  		""" + content +"""
  	  	</div>
	  	"""
	if bottom is not None:
		card += """
		<div class="mdl-card__actions mdl-card--border">
  	  		""" + bottom + """
  	  	</div>
	  	"""
	card += "</div>"
	return card

def new_table(headers = [], rows = []):
	headings = "<tr>"
	for heading in headers:
		headings += "<th>"+ heading +"</th>"
	headings += "</tr>"

	data = ""

	for row in rows:
		data += "<tr>"
		for column in row:
			data += "<td>"+ column +"</td>"
		data += "</tr>"

	return """
	<table class="mdl-data-table mdl-js-data-table mdl-shadow--2dp">
	  <thead>
	 	"""+ headings +"""
	  </thead>
	  <tbody>
	    """ + data +"""
	  </tbody>
	</table>
	"""

def new_text_input(label, name):
	return """<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
    <input class="mdl-textfield__input" type="text" name='""" + name + """'>
    <label class="mdl-textfield__label" >"""+ label +"""</label>
  </div>"""
