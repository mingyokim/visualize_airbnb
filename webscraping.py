import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://insideairbnb.com/get-the-data.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

def getLinks():
	dataLinks = []

	div = soup.find('div', class_='contentContainer')

	for table in div.find_all('table'):
		for tr in table.find('tbody').find_all('tr'):
			rowData = tr.find_all('td')
			if rowData[2].text == 'listings.csv':
				data = {'City': rowData[1].text, 'Link': rowData[2].a['href']}
				dataLinks.append(data)
				break

	return dataLinks

#print (dataLinks)
##  if tr.getAttribute(2).a.text == 'listings.csv':
##      data = {'City': tr.getAttribute(1).text, 'Link': tr.getAttribute(2).a['href']}
##      linkDict.append(data)
##  print(linkDict)
