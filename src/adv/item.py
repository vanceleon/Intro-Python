class Item:
    """Item base class."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_encounter(self, player):
        """Called every time the player encounters the item."""
        pass

    def on_take(self, player):
        """Called every time the player takes an item."""
        pass

    def __str__(self):
        """Convert to string."""
        return self.description

class Treasure(Item):
    """A treasure that adds to your score the first time you pick it up."""
    def __init__(self, name, description, value):
        self.value = value
        self.picked_up = False
        super().__init__(name, description)

    def on_take(self, player):
        if not self.picked_up:
            player.score += self.value
            self.picked_up = True
        super().on_take(self, player)

class LightSource(Item):
    def __init__(self, name, description):
        self.lightsource = True
        super().__init__(name, description)