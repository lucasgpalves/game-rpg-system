from models.items import Item
from random import randint

class Weapon(Item):
    
    def __init__(self, name, price, amount, weight, dice):
        super().__init__(name, price, amount, weight)
        self.dice = dice
    