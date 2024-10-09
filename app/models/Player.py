import random as rd

class Player:
    
    _health = None
    _attack = None
    _armor = None
    
    """ CONSTRUCTOR """
    def __init__(self, health, attack, armor):
        self._health = health
        self._attack = attack
        self._armor = armor
    
    """ METHODS """
    def tackle(self, enemy):
        chance = rd.randint(0, 7)
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
    

    
    