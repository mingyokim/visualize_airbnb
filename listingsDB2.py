import sqlite3
import csv
import urllib.request

conn = sqlite3.connect('listingsALL.db')
conn.isolation_level = None

url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-12-03/visualisations/listings.csv"
response = urllib.request.urlopen(url)
cr = csv.DictReader(response.read().decode('utf-8').splitlines())

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS new_york(lat REAL, long REAL, price REAL)")

def data_entry(latitude, longitude, price):
	c.execute("INSERT INTO new_york (lat, long, price) VALUES (?, ?, ?)", (latitude, longitude, price))

try: 
	c = conn.cursor()
	c.execute("begin")

	create_table()
	for row in cr:
		data_entry(row['latitude'], row['longitude'], row['price'])

	c.execute("commit")
	c.close()
	conn.close()
except:
	c.execute("rollback")	
