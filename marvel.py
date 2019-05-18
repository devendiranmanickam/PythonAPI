#!/usr/bin/python3

import requests
import argparse
import time
import hashlib

XAVIER = 'http://gateway.marvel.com/v1/public'

# create a hashing function
def hashbuilder(curtime, privkey, pubkey):
    return hashlib.md5((curtime+privkey+pubkey).encode('utf-8')).hexdigest()

def marvelcharcall(curtime, hashy, pubkey, lookmeup):
    marvelurl = XAVIER + '/characters'
    marvelurl += "?name="+lookmeup+"&ts="+curtime+"&apikey="+pubkey+"&hash="+hashy
    hulk = requests.get(marvelurl)
    return hulk.json()

def main():
    with open('marvel.pub') as pubkeyfile:
        beast = pubkeyfile.read()

    with open('marvel.priv') as privkeyfile:
        storm = privkeyfile.read()

    curtime = str(int(time.time()))

    charlook = input("What character are we looking up?")

    hashy = hashbuilder(curtime, storm, beast)

    print(marvelcharcall(curtime, hashy, beast, charlook))

main()