import string


with file('key.txt', 'r') as f:
	a = f.readall()
	a.replace(":", "")
	print a
