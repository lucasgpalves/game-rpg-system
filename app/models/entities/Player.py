from core import Dice
from models.entities import Entity
from random import randint

class Player(Entity):
    
    level = None
    xp = None
    inventory = None
    
    """ CONSTRUCTOR """
    def __init__(self, name, health, max_health, armor, movement, level, xp, inventory):
        super().__init__(name, health, max_health, armor, movement)
        self.level = level
        self.xp = xp
        self.inventory = inventory
    
    """ METHODS """
    def tackle(self, weapon, enemy, bonus = 0):
        if weapon not in self.inventory: # Verifica se existe arma no inventário
            raise ValueError('This weapon don\'t exists')
            
        chance = randint(0, 21) + bonus # Calcula chance de acerto
        
        if chance >= enemy.armor: # Verifica se acertou
            damage_weapon = Dice().throw_dices(weapon._dice)
            
            if chance >= 20 : ## Verica se foi crítico 
                damage = (damage_weapon + bonus) * 2
            else:
                damage = damage_weapon + bonus
            
            enemy.health -= damage # Reduz da vida do inimigo
            return damage
        
        return 0
    
    def healing(self, potion):
        if potion not in self.inventory: # Verifica se há poção no inventário
            raise ValueError('You don\'t have any potion in your inventory')
        
        if potion.amount <= 0: # Verificação adicional
            raise ValueError('You don\'t have more potion')         
        
        heal_amount = min(potion.heal, self.max_health - self.health) # Menor valor para agregar a vida atual
        self.health += heal_amount
        potion.amount -= 1 # Reduz a poção consumida
        
        if potion.amount == 0:
            self.inventory.remove(potion)
        
        return potion.heal
    