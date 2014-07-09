def count_string(string):
	s=0
	for letter in string:
		letter=1
		s=letter+s
	return s
print (count_string("Jona"))