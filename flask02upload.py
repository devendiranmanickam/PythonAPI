#!/usr/bin/python3

import re
import json
import smtplib
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from email.message import EmailMessage
import imghdr

## start a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to api server"

## make a API that allows for file attachmenets / uploads
## upload will be a pcap turned into JSON
@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def uploader():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        #return "File successfully uploaded!"
        return redirect(url_for("success"))

@app.route('/success')
def success():
    sipjson = []
    with open("PythonLog.log") as siplog:
        for line in siplog:
            sipobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if sipobj:
                lillist = []
                lillist.append(sipobj.group())
                lillist.append(sipobj.group(1))
                lillist.append(sipobj.group(2))
                lillist.append(sipobj.group(3))
                sipjson.append(lillist)
                # add match to list
        return json.dumps(sipjson)

@app.route("/emailsender")
def emailsender():
    msg = EmailMessage()
    msg['Subject'] = 'Graph data'
    msg['From'] = "test@hotmail.com"
    msg['To'] = "test@gmail.com"
    msg.preamble = "Here is the graph you requested"
    with open("2019-05-17-outage.png", "rb") as sendme:
        img_data = sendme.read()
    msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    with open("emailpassword.txt") as emailpass:
        myemailpass = emailpass.read()

    mail = smtplib.SMTP("smtp.live.com", 25)
    mail.starttls()
    mail.login('test@hotmail.com', myemailpass)
    mail.sendmail('test@hotmail.com', 'test@gmail.com', msg.as_string())
    mail.quit()
    return "Email sent!"

@app.route("/excel")
def excel():
    now = datetime.datetime.now()

    mdf = pd.read_excel('mydata.xlsx', sheet_name="Sheet1")
    #print(mdf.columns)
    #print(mdf['year'].values)
    #print(mdf['min'].values)

    xaxislist = list(mdf['year'].values)
    yaxislist = list(mdf['min'].values)


    #xaxislist = ["2016", "2017", "2018", "2019"]
    #yaxislist = [100, 2200, 4, 55]
    plt.ylabel("Downtime in minutes")
    plt.xlabel("Years")
    plt.title("Total amount of downtume in minutes in year!")
    plt.plot(xaxislist, yaxislist)
    plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
    return "Excel data saved into graph!"

if __name__ == "__main__":
    app.run(port=5006)
