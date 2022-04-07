import psycopg2
import xml.etree.ElementTree as ET

conn = psycopg2.connect("dbname=tracks user=postgres password=mayalove")
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    artist_id INT,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    title TEXT,
    album_id INT,
    len INT,
    rating INT,
    count INT
)
''')

filename = input('Input file path: ')
if len(filename) < 1: filename = 'C:\projects\py_learning\Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(filename)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    #print(name,artist,album,count,rating,length)

    cur.execute('INSERT INTO Artist (name) VALUES (%s) ON CONFLICT (name) DO NOTHING', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name=%s', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT INTO Album (title,artist_id) VALUES (%s,%s) ON CONFLICT (title) DO NOTHING', (album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title=%s', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT INTO Track (title,album_id,len,rating,count) VALUES (%s,%s,%s,%s,%s)', (name, album_id, length, rating, count))

    conn.commit()