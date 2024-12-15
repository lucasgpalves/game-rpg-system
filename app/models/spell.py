"""
    Name        The name of spell
    Casting     time the amount of time required to cast the spell
    Distance    The distance in meters that the spell can reach
    Component   The elements required to cast the spell (e.g., verbal, somatic, or material). If the
                component includes material items, they must be specified.
    Duration    The number of turns the spell remains active or in effect.
"""
import math

from ._component import Component
from .item import Item
from ._speel_shape import SpellShape
from .dice import Dice

from typing import List

class Spell:
    
    def __init__(self, name: str, 
                 casting_time: int, 
                 distance: float, 
                 area: float, 
                 spell_shape: SpellShape, 
                 dice: Dice,
                 component: List[Component] = None, 
                 component_items: List[Item] = None, 
                 duration: int = 0):
        self.name = name
        self.casting_time = casting_time
        self.distance = distance
        self.area = area
        self.spell_shape = spell_shape
        self.dice = dice
        self.component = component if component else []
        self.component_items = component_items if component_items else []
        self.duration = duration
        
    def calculate_spell_area(self, width:int = 1) -> float:
        if isinstance(self.spell_shape, SpellShape):
            shape = self.spell_shape.value
            return math.floor(shape.calculate_area(self.area))
        else:
            raise ("Invalid shape")  
            
    def calculate_damage(self, amount: int, bonus):
        
        damage = Dice.throw_dices(self.dice, amount) + bonus
        
        return damage