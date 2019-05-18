#!/usr/bin/python3

LOOKUPAPI = r"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=75068&date=2019-05-14&" \
            "distance=25&API_KEY=D85797D9-977D-46A6-84E5-B4B343AA73ED"

import requests


def main():
    r = requests.get(LOOKUPAPI)

    evenlist = (r.json())[0::2]

    for day in evenlist:
        print(day['DateForecast'])
        print(day['ReportingArea'], day['StateCode'], sep=", ")
        print("Air quality is:", day['Category']['Name'])
        print(day['Discussion'])
        input("-- Press Enter to Continue --")
    #print(evenlist)

    #print(evenlist[0]['ReportingArea'])

main()
