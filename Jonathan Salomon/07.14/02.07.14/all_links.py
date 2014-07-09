page1=("'<a href=''http://www.yahoo.com'' /><link''<a href=''http://www.google.com'' /><link''<a href=''http://www.udacity.com'' /><link'")
def get_next_target(page):
	start_link=page.find("href")
	start_quote=page.find("''",start_link)+1
	end_quote=page.find("''",start_quote)
	url=page[start_quote:end_quote]
	return url,end_quote
def all_links(page):
	links=[]
	while(True):
		url,end_pos=get_next_target(page)
		if (url!="''"):
			if ("http://www.") in url:
				links.append(url)
				page=page[end_pos:]
			else:
				break
	return links
print (all_links(page1))