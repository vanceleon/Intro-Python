from room import Room
from player import Player
from items import Items
import textwrap
# Declare all the rooms

# {outside: {name: "", desc: ""}}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure':  Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


items = {
    'coins': Items("coins", "currency for transactions"),
    'compass': Items("compass", "tool for finding your direction")
    # 'compass': Items("compass", "tool for finding your direction")
    # 'compass': Items("compass", "tool for finding your direction")
    # 'compass': Items("compass", "tool for finding your direction")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# assigning the items to the room
room['outside'].items.append(items["compass"]) 
# room['foyer'].items.append(items["100 coins, "]) 
# room['overlook'].items.append(items["compass"]) 
# room['narrow'].items.append(items["compass"]) 
# room['teasure'].items.append(items["compass"]) 
# room[''].items = items["100 coins", "sword"] 
# room['outside'].items = items["rock", "map"] 
# room['foyer'].items = items["compass"] 
# room['treasure'].items = items["1000 coins", "sword"] 
# room['overlook'].items = items["shield"] 


# Main
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# d = Player(input("Where do you want to go? "))

s  = Player(input ("What is your name? "), room["outside"])

direction_dictionary = {"n": "north", "s": "south", "w": "west", "e": "east", "forward": "n", "backwards": "s", "right": "e", "left": "w"  }

while True: 
    print(f"You are currently in {s.currentRoom.name}")
    print(f"Description: {s.currentRoom.description}")
    print(f"Description: {s.currentRoom.items}")
    cmd = input("->").lower()
    if len(cmd) == 1:
        if cmd == "q":
            break
        elif cmd in direction_dictionary:
            s.currentRoom = getattr(s.currentRoom, f"{cmd}_to")
            print(f"You are currently in {s.currentRoom.name}")
            print(f"Description: {s.currentRoom.description}")
            print(f"Description: {s.currentRoom.items}")
        else: 
            print("I don't understand that command")
    else:
        if cmd == "look":
            if cmd == "q":
                s.look(direction_dictionary[cmd])
        else:
            print("I did not understand that command.") 

