
class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"\n\n{self.name}\n\n {self.description}\n"

    def on_drop(self):
        print(f"You have dropped {self.name}.")

class Food(Items):
    def __init__(self, name, description, calories):
        Items.__init__(self, name, description)
        self.calories = calories            
    
    def eat(self):
        return self.calories
    def on_drop(self):
        print(f"You have dropped {self.name}.\n")

    # def get(self, item):
    #     pick_up = self.name

