class Item:
    
    _name = None
    _price = None
    _amount = None
    
    def __init__(self, name, price, amount):
        self._name = name
        self._price = price
        self._amount = amount
        
    def __str__(self):
        return f'Name: {self._name}, Price: {self._price}, Amount: {self._amount}'
    
    def __repr__(self):
        return f'Name(name={self._name}, price={self._price}, amount={self._amount})'