#!/usr/bin/python3

def showInstructions():
    print('''
RPG Game
--------
Commands:
    go [directions]
    get [item]
    ''')

def showStatus():
    print('----------------------------------------------')
    print('You are in the ', currentRoom)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
    print('----------------------------------------------')

inventory = []

rooms = {'Hall':{'south':'Kitchen', 'east': 'Dining Room', 'item': 'key'},'Kitchen': {'north':'Hall', 'item': 'monster'}, 'Dining Room': {'west': 'Hall','item':'cookie'}}

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('> ')

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way!")
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print("you just picked up", move[1])
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get '+ move[1]+'!')
    # if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("A monster has got you... GAME OVER")
        break

print("Thanks for playing")
