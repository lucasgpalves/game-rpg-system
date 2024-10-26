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

from typing import List

class Spell:
    
    def __init__(self, name: str, casting_time: int, distance: float, area_radius: float, spell_shape: SpellShape, component: List[Component] = None, component_items: List[Item] = None, duration: int = 0):
        self.name = name
        self.casting_time = casting_time
        self.distance = distance
        self.area_radius = area_radius
        self.spell_shape = spell_shape
        self.component = component if component else []
        self.component_items = component_items if component_items else []
        self.duration = duration
        
    def calculate_spell_area(self, width:int = 1) -> float:
        
        shape = self.spell_shape
        area = self.area
        
        match (shape):
            case SpellShape.TRIANGLE:
                return (math.sqrt(3) / 4) * area ** 2
            case SpellShape.CIRCLE:
                return math.pi * (area ** 2)
            case SpellShape.SQUARE:
                return area ** 2
            case SpellShape.LINE:
                return area * width
            case _:
                raise ValueError("Invalid shape")