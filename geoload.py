import urllib.request, urllib.parse, urllib.error
import http
import psycopg2
import json
import time
import ssl
import sys

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

conn = psycopg2.connect('dbname=geoload user=postgres password=mayalove')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (adress TEXT, geodata TEXT)
''')

filehandle = open('C:\projects\py_learning\where.data')
count = 0
for line in filehandle:
    if count > 200:
        print('Retrieved 200 results, restart to retrieve more')
        break

    adress = line.strip()
    print(adress)