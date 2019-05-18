#!/usr/bin/python3
"""
Openstack JSON parsing
authon: rzfeeser@alta3.com
learning about json and python
"""

import json

def main():
    """runtime code"""
    with open(r'openstackresponse01.json', 'r') as openjson:
        print(openjson.read())
        openjson.seek(0)
        decodedopenjson = json.load(openjson)
        #print(decodedopenjson)
        print(decodedopenjson['server']['security_groups'][1]['name'])
main()
