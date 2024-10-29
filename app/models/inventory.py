from .item import Item

class Inventory:
    
    def __init__(self, slots: int):
        self.slots = slots
        self.list_items = []
        self.total_weight = 0
        
    def create_inventory(self):
        self.list_items = [0] * self.slots
        
    def display_inventory(self):
        for item in self.list_items:
            if isinstance(item, Item):
                print(item.__dict__)
            else: 
                print(item)
        
    def add_item(self, item: Item):
        for slot in range(len(self.list_items)):
            if self.list_items[slot] == 0:
                self.list_items[slot] = item
        raise ValueError('You don\'t have any slot in inventory')
    
    def calculate_total_weight(self):
        self.total_weight = 0
        for item in self.list_items:
            if isinstance(item, Item):
                self.total_weight += item.total_weight
        return self.total_weight
    
    def get_gold(self) -> Item:
        for item in self.list_items:
            if isinstance(item, Item) and item.__class__.__name__ == "Gold":
                return item
        
        raise ValueError('You don\t have gold')
    
    def remove_item(self, item: Item, amount: int):
        for slot in self.list_items:
            if self.list_items[slot] == item:
                self.reduce_item(item, amount, slot)
                break
        
        raise ValueError('Item not found in inventory')
    
    def reduce_item(self, item: Item, amount: int, slot: int):
        item.amount -= amount
        if item.amount <= 0:
            self.list_items[slot] = 0