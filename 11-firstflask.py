#!/usr/bin/python3
""" Author: Fitzjon ||| Purpose: First Flask with Learning Python"""

from flask import Flask

app = Flask(__name__) # ALWAYS do this in your flask script

@app.route("/") # when you goto thje ROOT of your server... do the following
def endoftheday(): # function to trigger at ROOT
    return "Class is nearing the end for Wednesday"

if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
