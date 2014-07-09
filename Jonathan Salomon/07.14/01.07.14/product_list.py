liste=[2,3,4,5,7]
def product_list(list):
	s=1
	for number in list:
		s=s*number
	return s
print (product_list(liste))