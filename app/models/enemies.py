from ._entity import Entity

from typing import List, Dict

class Enemie(Entity):
    
    def __init__(self, name: str,
                 health: float, 
                 max_health: float, 
                 armor: int, 
                 movement: int, 
                 moves: List[Dict[str]]
                ):
        super().__init__(name, health, max_health, armor, movement)
        self.moves = moves if moves != None else []