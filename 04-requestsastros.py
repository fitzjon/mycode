#!/usr/bin/python3
""" FitzJon | author: jonathan.fitz@vzw.com | learning about API requests"""

# Import JSON and Ability to pull API  BUT NOW WITH REQUESTS MODULE
import requests

# Constant for JSON API File
MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    try:

        # make request 
        resp = requests.get(MAJORTOM)
        # CAN ALSO DO pyj = requests.get(MAJORTOM).json()   THEN GET RID OF PYJ = resp.json()

        # convert string data to JSON
        pyj = resp.json()

        # Parse out JSON attached we stripped off the response from the API
        # print(pyj)
        astrocosmo = pyj.get("people")

        # display selected data on screen - names of people in space /
        print("CURRENTLY IN SPACE:")
        for spaceperson in astrocosmo:
            print(spaceperson["name"])

    except:
        print("API is unavailable at the moment")

if __name__ == "__main__":
    main()
