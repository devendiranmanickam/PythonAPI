#!/usr/bin/python3

import requests
import webbrowser

# https://api.spacexdata.com/v3/launches/latest
# mission_name
# launch_date_local
# launch_success

res = requests.get(r'https://api.spacexdata.com/v3/launches/latest').json()

print('\n Mission name:', res['mission_name'])
print('\n Launch date:', res['launch_date_local'])
print('\n Launch success?', res['launch_success'])

input('\n\nPress ENTER to continue...')
# print('\n Video link is',res['links']['video_link'])
webbrowser.open(res['links']['video_link'])
