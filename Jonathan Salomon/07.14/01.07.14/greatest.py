liste1=[1,2,3,4,9,5]
liste2=[]
def greatest(list):
	s=0
	for number in list:
		if (s<number):
			s=number
	return s
	if (list==[]):
		return 0
print (greatest(liste1))
print (greatest(liste2))