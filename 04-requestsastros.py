#!/usr/bin/python3
""" FitzJon | author: jonathan.fitz@vzw.com | learning about API requests"""

# Import JSON and Ability to pull API 
import json
import urllib.request

# Constant for JSON API File
MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    # make request 
    resp = urllib.request.urlopen(MAJORTOM)
    
    # make python fetch out JSON data set from the API from 200 response
    jstring = resp.read()

    # convert string data to JSON
    pyj = json.loads(jstring.decode('utf-8'))

    # Parse out JSON attached we stripped off the response from the API
    print(pyj)
    astrocosmo = pyj.get("people")

    # display selected data on screen - names of people in space /
    print("CURRENTLY IN SPACE:")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])


if __name__ == "__main__":
    main()
