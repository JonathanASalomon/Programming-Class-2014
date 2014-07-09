page1=('<a href="http://www.yahoo.com">Yahoo</a><a href="http://www.google.com"</a>Google<a href="http://www.udacity.com">Udacity</a><a href="http;//wwww.facebook.com">Facebook</a><a href="http://www.youtube.com">Youtube</a>')

def get_next_target(page):
	start_link=page.find("href")
	start_quote=page.find('"',start_link)+1
	end_quote=page.find('"',start_quote)
	url=page[start_quote:end_quote]
	return url,end_quote

def all_links(page):
	links=[]
	while(True):
		url,end_pos=get_next_target(page)
		if (url!='"'):
			if ("http://www.") in url:
				links.append(url)
				page=page[end_pos:]
			else:
				break
	return links

user_input1=input('Entrez votre lien: ')

def search(user_input,page):
	links=all_links(page)
	for e in links:
		if user_input in e:
			return e
		else:
			return "Ce lien n'est pas dans la liste. Veuillez essayer google."

print (search(user_input1,page1))
