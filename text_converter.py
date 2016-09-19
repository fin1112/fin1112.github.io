def html_maker(text):
	for i in text:
		if i == "	":
			i = "   "

print html_maker("	To begin")