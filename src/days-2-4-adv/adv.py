from room import Room
from player import Player
from items import Items, Food
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
    'compass': Items("compass", "tool for finding your direction"),
    'lantern': Items("lantern", "Make sure you keep this to see in the darkness"),
    'sword': Items("compass", "tool for finding your direction"),
    'compass': Items("compass", "tool for finding your direction"),
    'bread': Food("bread", "Loaf of bread", 100),
    'meat': Food("meat", "1lb tri-tip", 500)
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

