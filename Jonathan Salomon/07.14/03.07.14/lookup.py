index1=[]
def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0]==keyword:
			entry[1].append(url)
	
	index.append([keyword,[url]])

add_to_index(index1,"Udacity","http://udacity.org")
add_to_index(index1,"Computing","http://acm.org")
add_to_index(index1,"Udacity","http://npr.org")

def lookup(index,keyword):
	for entry in index:
		if entry[0]==keyword:
			return entry[1]
print (lookup(index1,"Udacity"))
print (lookup(index1,"Computing"))