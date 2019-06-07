#!/usr/bin/python3

import json, time, sqlite3, requests

def walmartlookup(walmarturl, mykey, upckey):
    try:
        walmarturlobj = requests.get(walmarturl + mykey + upckey)
        return walmarturlobj.json()
    except:
        return False

def trackmeplease(tracktime, trackprice):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME VARCHAR2 PRIMARY KEY NOT NULL,
        PRICE REAL NOT NULL);''')
    except:
        pass
    conn.execute("INSERT INTO PRICE (TIME,PRICE) VALUES (?,?)",(tracktime, trackprice))
    conn.commit()
    cursor = conn.execute("SELECT time, price from PRICE")
    for row in cursor:
        print("TIME =", row[0])
        print("PRICE =", row[1])
    print("DATABASE OPERATION COMPLETE!!")
    conn.close()

def main():
    wurl = 'http://api.walmartlabs.com/v1/items?'
    wkey = '5mnbr76b2kshnsw2ex2vx6n8'
    wkey = 'apiKey=' + wkey
    wupc = '190198511270' # apple watch
    wupc = "&upc=" + wupc

    print("Walmart Query url is: ", wurl, wkey, wupc, sep="")

    decodedwalmart = walmartlookup(wurl, wkey, wupc)

    if decodedwalmart:
        print("\nWalmart Price on", time.ctime(), ": $", str(decodedwalmart['items'][0]['salePrice']))
        print(decodedwalmart)
        print(decodedwalmart.get(str(['items'][0]['msrp'])))
        #print("\nMSRP on", time.ctime(), ": $", str(decodedwalmart['items'][0]['msrp']))
        trackmeplease(time.ctime(), decodedwalmart['items'][0]['salePrice'])
    else:
        print("Something went wrong with the API Lookiup")

if __name__ == "__main__":
    main()

