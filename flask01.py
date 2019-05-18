#!/usr/bin/python3

import csv
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def vzw():
    return "Welcome to API automation"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello "+name

@app.route("/v1/csvwithout/")
def mycsvparse():  ## without header
    biglist = []
    with open('mycsv.csv') as csvtoparse:
        csv_reader = csv.reader(csvtoparse, delimiter=',')
        for row in csv_reader:
            littlelist = []
            littlelist.append(row[1])
            littlelist.append(row[3])
            biglist.append(littlelist)
    return json.dumps(biglist)

@app.route("/v1/csvwith/")
def mycsvwithheaderparse():  ## with header
    biglist = []
    with open('mycsvwith.csv') as csvtoparse:
        csv_reader = csv.DictReader(csvtoparse, delimiter=',')
        for row in csv_reader:
            littlelist = []
            littlelist.append(row['ip'])
            littlelist.append(row['port'])
            biglist.append(littlelist)
    return json.dumps(biglist)

@app.route("/v1/csv/<file>")
def mycsvargparse(file):  ## without header and file name as arg
    biglist = []
    try:
        with open(file) as csvtoparse:
            csv_reader = csv.reader(csvtoparse, delimiter=',')
            for row in csv_reader:
                littlelist = []
                littlelist.append(row[1])
                littlelist.append(row[3])
                biglist.append(littlelist)
        return json.dumps(biglist)
    except:
        return 'Something went wrong!'

if __name__ == "__main__":
    app.run(port=5006)

