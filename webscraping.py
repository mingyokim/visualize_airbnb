import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://insideairbnb.com/get-the-data.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

def findLinks():
    dataLinks = []
    div = soup.find('div', class_='contentContainer') #Only finds the section with the downloads
    for table in div.find_all('table'): #Iterates through all the tables on the page (one per city)
        for tr in table.find('tbody').find_all('tr'): #Iterates through each row of the table to find the data we want
            rowData = tr.find_all('td') #Puts all the table data in an object to make it easier to access data in a given index
            if rowData[2].text == 'listings.csv': #Column 3 contains the 'type' of data i.e. a csv file
                data = {'City': rowData[1].text, 'Link': rowData[2].a['href']} #Adds to a dictionary 
                dataLinks.append(data) #Adds that dictionary to a list
                break
    return dataLinks



