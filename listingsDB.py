import sqlite3
import csv
import urllib.request
from webscraping import getLinks

conn = sqlite3.connect('listingsALL.db')
conn.isolation_level = None

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS new_york(lat REAL, long REAL, price REAL)")

def data_entry(latitude, longitude, price):
	c.execute("INSERT INTO new_york (lat, long, price) VALUES (?, ?, ?)", (latitude, longitude, price))

dataLinks = getLinks();

try:
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS new_york")
	c.execute("begin")


	for link in dataLinks
		response = urllib.request.urlopen(link)
		cr = csv.DictReader(response.read().decode('utf-8').splitlines())
		
		create_table()
		for row in cr:
			data_entry(row['latitude'], row['longitude'], row['price'])
		break
	c.execute("commit")
	c.close()
	conn.close()
except:
	c.execute("rollback")

