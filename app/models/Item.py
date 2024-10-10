class Item:
    
    _name = None
    _price = None
    _amount = None
    
    def __init__(self, name, price, amount):
        self._name = name
        self._price = price
        self._amount = amount