    # Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    def __init__(self, name, roomStart, startingItems=[]):
        self.name = name
        self.currentRoom = roomStart
        self.inventory = startingItems
        self.strength = 15


    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not "":
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move in that direction")
    def look(self, direction=""):
        if direction is "":
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not "":
                print(nextRoom)
            else: 
                print("There is nothing there")
    def checkStatus(self):
        print(f"Your name is {self.name}, your strength is {self.strength}")
    
    def checkInventory(self):
        print("You are carrying: \n")
        for inventory in self.inventory:
            print(f"{inventory.name} - {inventory.description}")

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)

    def findItemByName(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None

    def hasLight(self):
        return True

    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None: 
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("You are not holding anything")