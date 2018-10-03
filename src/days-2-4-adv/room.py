# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player


class Room:
    def __init__(self, name, description, items):     
        self.name = name
        self.description = description
        self.n_to = ""
        self.s_to = ""
        self.w_to = ""
        self.e_to = ""
        self.items = []
        # self.items = [sword, coins, puppies, rock]


    def __str__(self):
        return f"\n\n{self.name}\n\n {self.description}\n\n {self.items}\n"
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




"""
# A given room object
example = {
    name: 'chuckecheese',
    description: 'cheesist place on earth',
    n_to: <Room Disneyland>
    s_to: <Room Zoo>
    w_to: ""
    e_to: <Room Knotts>
}
"""