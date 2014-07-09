page1=("")
	while (true):
		url,end pos=get_next_target(page)
		if url:
			return url
			page=page[end pos:]
		else:
			break
print (print_all_links(page1))			