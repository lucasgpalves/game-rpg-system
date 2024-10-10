from random import randint

class Dice:
    
    _sides = None
    
    def __init__(self, sides):
        self._sides = sides
        
    def throw_dices(self, amount):
        results = [randint(1, self._sides) for value in range(amount)]
        
        print(f'Foi jogado {amount} dados de {self._sides} lados')
        
        # for dice in range(amount):
        #     value = randint(1, self._sides)
        #     results.append(value)
            
        print(results)
        