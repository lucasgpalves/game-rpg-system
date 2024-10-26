from ._entity import Entity

from typing import List

class Enemie(Entity):
    
    def __init__(self, name: str, health: float, max_health: float, armor: int, movement: int, move: List[str]):
        super().__init__(name, health, max_health, armor, movement)
        self.move = move if move != None else []