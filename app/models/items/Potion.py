from models.items import Item

class Potion(Item) :
    
    def __init__(self, heal, name, price, amount, weight):
        super().__init__(name, price, amount, weight)
        self.heal = heal
    
    def to_string(self):
        print(
            f'\nNome: {self.name}'
            f'\nPreço: {self.price}'
            f'\nQtd: {self.amount}'
            f'\nCura: {self.heal}'
        )