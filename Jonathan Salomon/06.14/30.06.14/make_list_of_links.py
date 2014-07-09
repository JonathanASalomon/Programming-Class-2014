page1=("")
def make_list_of_links(page):
	while (true):
		links=[]
		url,end pos=get_next_target(page)
		if url:
			link.append(url)
			page=page[end pos:]
		else:
			break
	return links
print (make_list_of_links(page1))