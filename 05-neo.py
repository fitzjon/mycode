#!/usr/bin/python3
""" Fitzjon " Learning about NASA and DEV Keys using NEO """

import requests
import pprint

MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def getkey():
    with open("/home/student/nasa.key", "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')
        


def main():
    # Harvest our key from nasa.key in /home/student/nasa.key
    nasakey = getkey()

    # Append our key to MYAPI

    # Call the API  (request.get()) and pull of json (.json())
    # asteroidz = request.get(MYAPI + nasakey).json()
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()


    # Decode json - loop across "near_earth_objects" to reveal asteroids
    #pprint.pprint(asteroidz["near_earth_objects"])
    for bigrock in asteroidz["near_earth_objects"]:
        #print(bigrock["is_potentially_hazardous_asteroid"])
        if bigrock["is_potentially_hazardous_asteroid"]:
            print("Name - ", bigrock["name"])
            print("Proximity - ", bigrock["close_approach_data"])
            print("Size - ", bigrock["estimated_diameter"], end="\n*********\n")
            
        # else:
            # print("Go back to bed, nothing to worry about")



    # only those that display a danger where hazard is set to "True" 

if __name__ == "__main__":
    main()
