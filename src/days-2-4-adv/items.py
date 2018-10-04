
class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"\n\n{self.name}\n\n {self.description}\n"
    
    # def get(self, item):
    #     pick_up = self.name

