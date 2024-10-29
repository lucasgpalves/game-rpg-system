class Item:
    
    def __init__(self, name: str, price: float, amount: int, weight: float):
        self.name = name.capitalize()
        self.price = price
        self.amount = amount
        self.weight = weight
        
    @property
    def total_weight(self):
        return self.weight * self.amount