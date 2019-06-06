#!/usr/bin/python3
""" Author: Fitzjon ||| Purpose: First Flask with Learning Python"""

from flask import Flask

app = Flask(__name__) # ALWAYS do this in your flask script

@app.route("/") # when you goto thje ROOT of your server... do the following
def endoftheday(): # function to trigger at ROOT
    return "Class is just starting for Thursday"

@app.route("/hello/<name>", defaults={'position': 'Administrative Assitant'})
@app.route("/hello/<name>/<position>")
def hellostudents(name, position):# returns the name of whatever is entered after /hello/
    return " Hello {1} {0}. I am please to meet you {0}".format(name, position)
    #return "Hello {}".format(name)
    #return  "WELCOME TO CLASS..." + name



if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
