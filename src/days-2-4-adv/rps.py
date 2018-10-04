```
# Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    # enable the printing of items
    def __str__(self):
        return self.name
    # printing that you have dropped the items
    def on_drop(self):
        print(f"You have dropped {self.name}.")
# adding a food class to items 
class Food(Item):
    def __init__(self, name, description, calories):
        Item.__init__(self, name, description)
        self.calories = calories
    def eat(self):
        return self.calories
    def on_drop(self):
        print(f"You have dropped {self.name}.\nIt's not nice to play with your food!")
# egg for the bonus
class Egg(Food):
    def __init__(self):
        self.name = "Egg"
        self.description = "This is an egg."
        self.calories = 50
    def eat(self):
        return 0
    def on_drop(self):
        self.name = "Broken Egg"
        self.description = "This is a broken egg."
        print(f"You have dropped an egg and now it's broken.")
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    # enables the print in the prompt
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n\n{self.getItemsString()}\n"
    
    # light functionality
    def printRoomDescription(self, player):
        if player.hasLight():
            print(str(self))
        else:
            print("You cannot see anything.")
    
    # returns the items in the items array for the prompt
    def getItemsString(self):
        return f"The room contains: {', '.join([item.name for item in self.items])}"
    
    # ability to navigate the rooms
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    
    # adding items to the rooms 
    def addItem(self, item):
        self.items.append(item)

    #removing the items from the rooms    
    def removeItem(self, item):
        self.items.remove(item)
    
    # checking the items in the array and sending cmd through lowercasing
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

# Player class
class Player:
    # possibly have to remove and setup startingItems like the Room class
    def __init__(self, name, currentRoom, startingItems=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = startingItems
        # keeping track of the strength of the player
        self.strength = 10

    # moving player through the rooms 
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(player)
        # edge casing if the room doesn't exist
        else:
            print("You cannot move in that direction.")
    
    # adding ability to look 
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(player)
        # else contains look functionality
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            # looking into the next room
            if nextRoom is not None:
                nextRoom.printRoomDescription(player)
            # edge case
            else:
                print("There is nothing there.")
    
    # checking the status of the player
    def printStatus(self):
        print(f"Your name is {self.name}, your strength is {self.strength}")
    
    # checking the inventory the player has 
    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"  {item.name} - {item.description}\n")
    
    # adding items to the player
    def addItem(self, item):
        self.items.append(item)
    
    # removing the items from the player
    def removeItem(self, item):
        self.items.remove(item)

    # checking the items to see if the item exists
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    # checking the players to see if he has light
    def hasLight(self):
        return True
    
    # dropping the items
    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            # adding the item the player drops to the room
            self.currentRoom.addItem(itemToDrop)
            # printing the dropped item
            itemToDrop.on_drop()
        else:
            print("You are not holding that item.")



# adv file
from room import Room
from player import Player
from item import Item, Food, Egg
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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# items that are hard coded 
rock1 = Item("Rock", "This is a rock.")
big_rock = Item("Big Rock", "This is a big rock.")
bread = Food("Bread", "This is a loaf of bread.", 100)

egg = Egg()
playerStartingItems = [rock1]

# assigning each item to each room
room['outside'].addItem(big_rock)
room['foyer'].addItem(bread)
room['treasure'].addItem(egg)


# dictionary that contains valid directions for the player
valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

# Beginning Prompt 
player = Player(input("What is your name? "), room['outside'], playerStartingItems)

# starting place
print(player.currentRoom)
while True:
    # sending all cmds to lowercase
    cmds = input("-> ").lower().split(" ")
    # if cmd has one letter at the beginning it will run the following cmds
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        # running through valid directions
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        # code might not need to be there
        elif cmds[0] == "look":
            player.look()
        # checking inventory
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        # checking the status of the player
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("I did not understand that command.")
    # word commands ex take look 
    else:
        # looking to the next room
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        # testing for variations of take 
        elif cmds[0] == "take" or cmds[0] == "get":
            
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            # testing to see if the item is there and not none
            if itemToTake is not None:
                # in the player class these functions are invoked by the command
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have picked up {itemToTake.name}")
            # edge case if the item is not there
            else:
                print("You do not see that item.")
        # drop command
        elif cmds[0] == "drop":
            player.dropItem(cmds[1:])
        
        # eat command to boost the players strength
        elif cmds[0] == "eat":
            # finding the item in the array
            itemToEat = player.findItemByName(" ".join(cmds[1:]))
            # if the item exists 
            if itemToEat is not None and hasattr(itemToEat, "eat") and 
            # testing to see if the calories is greater than zero
            itemToEat.eat() > 0:
                # adjusting the calorie count to strength for the player
                strengthGain = int(itemToEat.eat() / 10)
                # adding strenght to current strenght
                player.strength += strengthGain
                # deletes the item after you eat it
                player.removeItem(itemToEat)
                del itemToEat
                print(f"You have gained {strengthGain} strength!")
            # edge case for items that you can't eat
            else:
                print("You cannot eat that.")
        # edge to edge case, command is just not there in the game, ultimately to keep the program running and not erroring out
        else:
            print("I did not understand that command.")