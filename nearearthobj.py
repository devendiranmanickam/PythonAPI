#!/usr/bin/python3

"""learnig about near earth objects from NASA"""

import requests
import pprint

# define API key (read from file)
with open('nasaapi.key') as keyFile:
    mykey = keyFile.read()

stdate = input("enter start date in YYYY-MM-DD format: ")
enddate =  input("enter end date in YYYY-MM-DD format: ")

# lookup NASA API
# https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY
res = requests.get(r'https://api.nasa.gov/neo/rest/v1/feed?api_key='+mykey+'&start_date='+stdate+'&end_date='+enddate)


# dump initial data to screen
pprint.pprint(res.json())

res = res.json()

# custom print
for eachdate in res['near_earth_objects']:
    print("\nresults for date:", eachdate)
    for key in res['near_earth_objects'][eachdate][0]:
        if res['near_earth_objects'][eachdate][0]['is_potentially_hazardous_asteroid'] == True:
            if key == 'estimated_diameter':
                #print("\nestimated diameter:",res['near_earth_objects'][eachdate][0][key])
                for key2 in res['near_earth_objects'][eachdate][0][key]:
                    if key2 == 'miles':
                        print(res['near_earth_objects'][eachdate][0][key][key2])




