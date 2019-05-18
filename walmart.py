#!/usr/bin/python3

import requests
import pprint
import sqlite3
import time

WUPC = 'http://api.walmartlabs.com/v1/items?'
APIKEY = 'apiKey=d7hjdvye4sky5cdwmmmtf3bf'


def upclookup(upc):
    res = requests.get(WUPC+APIKEY+upc)
    if res.status_code == 200:
        return res.json()
    else:
        return False


def trackmeplease(trackt, trackp):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE (TIME VARCHAR2 PRIMARY KEY NOT NULL, PRICE REAL NOT NULL);''')
    except:
        pass
    conn.execute("INSERT INTO PRICE (TIME,PRICE) VALUES (?,?)", (trackt, trackp))
    conn.commit()
    cursor = conn.execute("SELECT time, price from PRICE")
    for row in cursor:
        print("\nTIME = ", row[0])
        print("PRICE = ", row[1])

    print("Database operation done")
    conn.close()

def main():
    upc = input("what is the UPC you wish to lookup? ")
    upc = "&upc=" + upc
    resp = upclookup(upc)
    if resp:
        #print(resp)
        #pprint.pprint(resp)
        print('\nItem name:', resp['items'][0]['name'])
        print('Item description:', resp['items'][0]['shortDescription'])
        print('Price: $', resp['items'][0]['salePrice'], sep='')

        savetodb = input("Save to database? (y/n) ")
        if savetodb.strip().lower() == 'y':
            trackmeplease(time.ctime(), resp['items'][0]['salePrice'])

    else:
        print('Something went wrong!')

main()


