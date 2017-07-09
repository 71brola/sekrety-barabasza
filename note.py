def read_note(name):
	return open(name,"r").read()


def write_note(name,content):
	open(name,"w").write(content)



