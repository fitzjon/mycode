#!/usr/bin/python3
"""Author: FitzJon | Email: jonathan.fitz@verizonwireless.com || learning json with python"""

# python has no json support
#with python, the jspnbatteries are in the box, but you need to plug them in
import json

def main():
    # define a list of dictionaries
    videogames = [{"game1": "red dead redemtpion", "game2": "War Craft", "game3": "StarCraft", "game4": "Diablo"}, {"game1": "paperboy", "game2": "Top Gun"}]

    # SHOW THE VALUE OF VIDEOGAMES
    print(videogames)

    # create a local file
    with open("videogames.json", "w") as vidfile: # "w" = write, "r" = read, "a" = append
        json.dump(videogames, vidfile)

if __name__ == "__main__": 
    main()
