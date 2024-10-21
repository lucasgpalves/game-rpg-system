from .item import Item

class Potion(Item) :
    
    def __init__(self, heal: int, name: str, price: float, amount:int, weight: float):
        super().__init__(name, price, amount, weight)
        self.heal = heal
    
    def to_string(self):
        print(
            f'\nNome: {self.name}'
            f'\nPreço: {self.price}'
            f'\nQtd: {self.amount}'
            f'\nCura: {self.heal}'
        )