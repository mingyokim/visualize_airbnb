import sqlite3
import csv
import urllib.request
from webscraping import getLinks

conn = sqlite3.connect('listingsALL1.db')
conn.isolation_level = None

def create_table(city):
	query = "CREATE TABLE IF NOT EXISTS '%s' (lat REAL, long REAL, price REAL)" % (city)
	c.execute(query)
	print(query)

def data_entry(city, latitude, longitude, price):
	query = "INSERT INTO '%s' (lat, long, price) VALUES (?, ?, ?)" % (city)
	c.execute(query, (latitude, longitude, price))
	#print(query)

dataLinks = getLinks();
print(dataLinks)
try:
	c = conn.cursor()
	#print("hello")
	c.execute("DROP TABLE IF EXISTS Amsterdam")
	#print("drop")
	c.execute("begin")
	#print("begin")		
	for dataObj in dataLinks:
		#print(dataObj)
		#if dataObj['City'] != 'Trentino':
		#	continue
		try:
			response = urllib.request.urlopen(dataObj['Link'])
		except:
			response = urllib.request.urlopen(urllib.parse.quote(dataObj['Link'].encode('utf-8'),':/')) 
				
		#print(dataObj['Link'])
		cr = csv.DictReader(response.read().decode('utf-8').splitlines())
	
		create_table(dataObj['City'])
		for row in cr:
			data_entry(dataObj['City'], row['latitude'], row['longitude'], row['price'])

	c.execute("commit")
	c.close()
	conn.close()
except:
	print("error")
	c.execute("rollback")
