from models.items import Item

class Potion(Item) :
    
    _heal = None
    
    def __init__(self, heal, name, price, amount):
        super().__init__(name, price, amount)
        self._heal = heal
        
    @property
    def heal(self):
        return self._heal
    
    def to_string(self):
        print(
            f'\nNome: {self._name}'
            f'\nPreço: {self._price}'
            f'\nQtd: {self._amount}'
            f'\nCura: {self._heal}'
        )