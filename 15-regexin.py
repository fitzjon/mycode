#!/usr/bin/python3
""" Author: Fitzjon ||| Purpose: Learning RegEx in Python """

import re

def main():
    with open("testcap.txt", "r") as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if regmatch:
                print(regmatch) ## display match object
                print(regmatch.group()) ## display the full match
                print(regmatch.group(1)) ## display the digit of the caller
                print(regmatch.group(2)) ## display the IPv6 IP
                print(regmatch.group(3)) ## display the Port # 

if __name__ == "__main__":
    main()
