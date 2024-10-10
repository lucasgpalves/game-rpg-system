from models.entities import Entity
from random import randint

class Player(Entity):
    
    _health = None
    _attack = None
    _armor = None
    
    """ CONSTRUCTOR """
    def __init__(self, name, health, attack, armor):
        super().__init__(name, health)
        self._attack = attack
        self._armor = armor
    
    """ METHODS """
    def tackle(self, enemy, bonus = 0):
        chance = randint(0, 7) + bonus # caso haja bonus seria somado
        print(chance)
        if chance >= enemy.armor:
            if chance == 6 :
                damage = self.attack * 2
            else:
                damage = self.attack
            
            enemy.health -= damage
            return damage
        
        return 0
    
    def healing(self, potion):
        self.health += potion.heal
        
        potion._amount -= 1
        
        return potion.heal
        
    """ GETTER and SETTER """
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        self._health = health
    
    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, attack):
        self._attack = attack
    
    @property
    def armor(self):
        return self._armor
    
    @armor.setter
    def armor(self, armor):
        self._armor = armor
    

    
    