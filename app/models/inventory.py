from .item import Item

class Inventory:
    
    def __init__(self, slots: int):
        self.slots = slots
        self.list_items = []
        
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
            if self.list_items[slot] != 0:
                continue
            else: 
                self.list_items[slot] = item
                break
            
    def remove_item(self, item: Item):
        return None