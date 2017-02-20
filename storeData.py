from webscraping import findLinks
import csv
import urllib.parse
import sqlite3

conn = sqlite3.connect('listingsALL.db')
conn.isolation_level = None

def create_table(city):
	c.execute("CREATE TABLE IF NOT EXISTS " + city + "(lat REAL, long REAL, price REAL)")

def data_entry(latitude, longitude, price, city):
	c.execute("INSERT INTO " + city + "(lat, long, price) VALUES (?, ?, ?)", (latitude, longitude, price))


dataLinks = findLinks()
try:
   c = conn.cursor()
   c.execute('begin')
   for dataPair in dataLinks:
      try:
           url = dataPair['Link'].replace("ü","%C3%BC")
           city = dataPair['City'].replace(" ", "").replace(".","").replace(",","")
           print(city)
           c.execute("DROP TABLE IF EXISTS " + city)
           response = urllib.request.urlopen(url)
           cr = csv.DictReader(response.read().decode('UTF-8').splitlines())
           create_table(city)
           for row in cr:
               data_entry(row['latitude'], row['longitude'], row['price'], city)
      except:
         print('Error processing: ' + city + ' with url: ' + url)
   c.execute("commit")
   c.close()
   conn.close()
except:
   c.execute("rollback")
