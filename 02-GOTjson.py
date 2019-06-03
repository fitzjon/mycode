#!/usr/bin/python3
""" Author: Fitzjon | Email: jonathan.fitz@verizonwireless.com | Learing GOTjson.py"""

#Pull in json so we can parse json
import json

def main():
    # open the jonsnow.json file in read mode
    with open ("jonsnow.json", "r") as gotdata:
    
        jonsnow = gotdata.read() #create a STRING of all the json
        GOTpy = json.loads(jonsnow) # convert STRING to pythonic LISTs and DICTs
    print(GOTpy) # display the GOTpy data
    print(GOTpy["url"]) # display values assoc. with URL
    print(GOTpy["titles"][0]) # display values assoc. with Titles & only show 0 item
    
    # creata a loop to move across aliases
    with open("aliases.txt", "w") as jsaliases:
        for GOTalias in GOTpy["aliases"]: 
            print(GOTalias, file=jsaliases)
            print(GOTalias)
    print(GOTpy["aliases"])  # display values assoc. with Aliases 
        #print(jonsnow)
    # parse jonsnow.json file for...
    # display character name
    # display character alias / titles 
    # display the API for ???




if __name__ == "__main__":
    main()
