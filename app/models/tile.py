""" __sumary__
    height = altura = z
    width = largura = y 
    length = comprimento = x 
"""

class Tile:
    
    def __init__(self, name: str, height: int, width: int, length: int, is_breakable: bool, is_rigid: bool, health: int = -1, max_health: int = -1):
        self.name = name
        self.height = height
        self.width = width
        self.length = length
        self.is_breakable = is_breakable
        self.is_rigid = is_rigid
        self.health = health
        self.max_health = max_health
        
    def destroy(self) -> bool: 
        return self.health <= 0 and self.is_breakable
            
        