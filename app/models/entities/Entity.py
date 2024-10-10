class Entity:
    
    _name = None
    _health = None
    _armor = None
    _movement = None
    
    def __init__(self, name, health, armor, movement):
        self._name = name
        self._health = health
        self._armor = armor
        self._movement = movement