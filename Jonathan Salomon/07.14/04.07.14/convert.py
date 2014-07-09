def convert(n):
	h1=n/3600
	h=int(h1)
	m1=(h1-h)*60
	m=int(m1)
	s=int((m1-m)*60)
	return h,m,s
print (convert(14000))