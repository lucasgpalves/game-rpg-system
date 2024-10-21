from .item import Item
from random import randint
from .dice import Dice

class Weapon(Item):
    
    def __init__(self, name: str, price: float, amount: int, weight: float, dice: Dice):
        super().__init__(name, price, amount, weight)
        self.dice = dice
    