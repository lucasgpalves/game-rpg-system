class Item:
    
    def __init__(self, name: str, price: float, amount: int, weight: float):
        self.name = name
        self.price = price
        self.amount = amount
        self.weight = weight
        self.total_weight = weight * amount