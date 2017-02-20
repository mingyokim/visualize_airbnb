import sqlite3
import csv
import urllib.request
import urllib.parse

conn = sqlite3.connect('listingsTrentino.db')
conn.isolation_level = None

url = 'http://data.insideairbnb.com/italy/trentino-alto-adige-sdtirol/trentino/2015-10-12/visualisations/listings.csv'
response = None
try:
	response = urllib.request.urlopen(url)
except:
	response = urllib.request.urlopen(urllib.parse.quote(url))
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
