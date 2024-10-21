from random import randint

class Dice:
    
    def __init__(self, sides: int):
        self.sides = sides
        
    def throw_dices(self, amount):
        results = [randint(1, self.sides) for value in range(amount)]
        
        print(f'Foi jogado {amount} dados de {self.sides} lados')
            
        return results
        