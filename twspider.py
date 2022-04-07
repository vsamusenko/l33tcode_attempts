import twname2id
import json
import psycopg2
import requests
import os

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF3ITAEAAAAAGskO9llOe34t3EtU1s%2BSd3r%2FRAg%3DbYd9L5uK1ith2qHJCI4KlAZ5uJgwCvpw5TI6z1X9ULi2osHzuZ'

conn = psycopg2.connect('dbname=twspider_db user=postgres password=mayalove')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Twitter (
    name TEXT,
    retrieved INT,
    friends INT
)
''')

while True:
    tw_name = input('Input twitter name or type "quit" to exit: ')
    if (tw_name == 'quit'): break
    if (len(tw_name) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            tw_name = cur.fetchone()[0]
        except:
            print('No unretrieved accounts found')
            continue

    tw_id = twname2id.main(tw_name)
    url = 'https://api.twitter.com/2/users/{}/following'.format(tw_id)
    print('Retrieving', url, tw_name)

    response = requests.request("GET", url, auth=twname2id.bearer_oauth, params={'max_results':5})
    print(response.status_code)
    if response.status_code != 200:
        raise Exception('Request returned an error: {} {}'.format(response.status_code,response.text))

    response_json = response.json()

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name=%s', (tw_name,))

    for u in response_json['data']:
        friend=u['username']
        print(friend)

        countnew = 0
        countold = 0

        cur.execute('SELECT friends FROM Twitter WHERE name=%s LIMIT 1',(friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends=%s WHERE name=%s', (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (%s,0,1)',(friend,))
            countnew = countnew + 1

        print('New accounts:', countnew, 'revisited: ', countold)
        conn.commit()



