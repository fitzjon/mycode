#/usr/bin/python3
"""Author: Fitzjon ||| Purpose: Learning Python and CSV Reader"""

import csv

def main():
    with open('superhero.csv') as csvf:
        reader =csv.DictReader(csvf)
        for row in reader:
            print(row['heroname'], "drives a", row['car'])

if __name__ == "__main__":
    main()
