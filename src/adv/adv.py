import textwrap
from room import Room
from player import Player
from item import Treasure

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south."""),
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

# Add some items

t = Treasure("coins", "Shiny coins", 100)
room['overlook'].contents.append(t)

t = Treasure("silver", "Tarnished silver", 200)
room['treasure'].contents.append(t)


def tryDirection(d, curRoom):
    """
    Try to move a direction, or print an error if the player can't go that way.

    Returns the room the player has moved to (or the same room if the player
    didn't move).
    """
    attrib = d + '_to'

    # See if the room has the destination attribute
    if hasattr(curRoom, attrib):
        # If so, return its value (the next room)
        return getattr(curRoom, attrib)

    # Otherwise print an error and stay in the same room
    print("You can't go that way")

    return curRoom

def find_item(name, curRoom):
    """
    Search the current room to see if we can locate the treasure in question.
    """
    for i in curRoom.contents:
        if i.name == name:
            return i

    return None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

done = False

while not done:
    # Print the room name
    print("\n{}\n".format(player.curRoom.name))

    # Print the room description
    for line in textwrap.wrap(player.curRoom.description):
        print(line)

    # Print any items found in the room
    if len(player.curRoom.contents) > 0:
        print("\nYou also see:\n")
        for i in player.curRoom.contents:
            print("     " + str(i))

    # User prompt
    s = input("\nCommand> ").strip().lower().split()

    if len(s) > 2 or len(s) < 1:
        print("I don't understand that.")
        continue

    # Intransitive verbs
    if len(s) == 1:
        if s[0] == "quit" or s[0] == "q":
            done = True
        elif s[0] == "inventory" or s[0] == "i":
            if len(player.contents) == 0:
                print("You're not carrying anything.")
            else:
                print("You are carrying:\n")
                for i in player.contents:
                    print(f"    {i}")

        elif s[0] in ["n", "s", "w", "e"]:
            player.curRoom = tryDirection(s[0], player.curRoom)
        else:
            print("Unknown command {}".format(' '.join(s)))
    
    # Transitive verbs
    elif len(s) == 2:
        if s[0] == 'get' or s[0] == 'take':
            item = find_item(s[1], player.curRoom)
            if item == None:
                print("I don't see that here.")
            else:
                # Move from room to player
                player.curRoom.contents.remove(item)
                player.contents.append(item)
                print(f"{item}: taken.")

        elif s[0] == 'drop':
            item = find_item(s[1], player)
            if item == None:
                print("You're not carrying that.")
            else:
                # Move from player to room
                player.contents.remove(item)
                player.curRoom.contents.append(item)
                print(f"{item}: dropped.")
        else:
            print("Unknown command {}".format(' '.join(s)))