#/usr/bin/python3
"""Author: Fitzjon ||| Purpose: Learning Python and CSV Reader"""

import csv
import json

def main():
    jsonf = open('superhero.json', 'w')

    with open('superhero.csv') as csvf:
        reader =csv.DictReader(csvf)
        for row in reader:
                json.dump(list(reader), jsonf)
    jsonf.close() # Close the json

if __name__ == "__main__":
    main()
