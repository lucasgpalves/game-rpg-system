"""
Verificações utilizando not ou ! (em outras linguagens)
O uso de not reduz bastante a quantidade de funções aninhadas,
realizando uma parada quando necessário dentro do código por não se encaixar
dentro da condição.
Obs: Dependendo da regra de negócio o uso do not não é recomendado
"""

from ._entity import Entity

from .potion import Potion
from .inventory import Inventory
from .dice import Dice
from .weapon import Weapon
from ._status import Status
from random import randint

from typing import List

class Player(Entity):
    
    def __init__(self, name: str, health: float, max_health: float, armor: int, movement: int, level: int, xp: int, inventory: Inventory, status: List[Status] = None):
        super().__init__(name, health, max_health, armor, movement)
        self.level = level
        self.xp = xp
        self.inventory = inventory
        self.status = status if status else []
    
    def tackle(self, weapon, enemy, bonus = 0):
        if not isinstance(weapon, Weapon):
            raise ValueError('Invalid weapon')
        
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
        if not isinstance(potion, Potion):
            raise ValueError('The item what do you want use, is\ not a potion')
        
        if potion not in self.inventory: # Verifica se há poção no inventário
            raise ValueError('You don\'t have any potion in your inventory')
        
        if potion.amount <= 0: # Verificação adicional
            raise ValueError('You don\'t have more potion')         
        
        heal_amount = min(potion.heal, self.max_health - self.health) # Menor valor para agregar a vida atual
        self.health += heal_amount
        potion.amount -= 1 # Reduz a poção consumida
        
        if potion.amount == 0:
            self.inventory.remove(potion)
        
        return heal_amount

    
    def change_player_status(self, effect):
        self.status = effect
    