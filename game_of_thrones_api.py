#!/usr/bin/python3

import requests

# ask which book user want to query
book = input ("Enter book number : ")

# print name of the book
res = requests.get(r'https://www.anapioficeandfire.com/api/books/'+book).json()

print('name of the book is', res['name'])

print('\n Writing characters in ', res['name'],' to a file...')

with open(res['name'].replace(" ","_")+'.txt','w') as file:
    # print the characters
    for x in res['characters']:
        print(requests.get(x).json()['name'],file=file)