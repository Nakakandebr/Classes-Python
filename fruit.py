class Fruit:
    category = "Fresh fruit"
    
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        
    def ripen(self):
        return f" Bridget is washing the {self.color} {self.name}  which is a {self.category} now ."
    
    def rot(self):
        return f" They are Peeling the {self.color} {self.name} using a knife."
    
    def grow(self):
        return f" Children are eating the {self.color} {self.name} which cost  {self.price} dollars per pound."
    
    