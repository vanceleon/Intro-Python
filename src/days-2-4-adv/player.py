    # Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    def __init__(self, name, roomStart, startingItems=[]):
        self.name = name
        self.currentRoom = roomStart
        self.inventory = []

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

    # def pickup_item(self, inventory):
    #     if 

    # def dropoff(self, inventory):
