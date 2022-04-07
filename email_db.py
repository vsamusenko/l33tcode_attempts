import psycopg2

conn = psycopg2.connect("dbname=email_db user=postgres password=mayalove")
cur = conn.cursor()

cur.execute("drop table if exists Counts")

cur.execute("create table Counts (id serial PRIMARY KEY, email TEXT, count INT);")

filename = input('Input file path: ')
if len(filename)<1: filename = 'C:\projects\py_learning\mbox-short.txt'
filehandle = open(filename)
for line in filehandle:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('select count from Counts where email=%s',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into Counts (email,count) values (%s,1)',(email,))
    else:
        cur.execute('update Counts set count=count+1 where email=%s',(email,))
    conn.commit()

sqlstr = 'select email,count from Counts order by count desc limit 10'

cur.execute(sqlstr)
x = cur.fetchall()
for row in x:
    print(row[1], str(row[0]))


cur.close()
conn.close()