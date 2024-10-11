from models.items import Item

class Inventory:
    
    def __init__(self, slots):
        self.slots = slots
        self.list_items = []
        
    def create_inventory(self):
        for slot in range(self.slots):
            self.list_items.append(0)
        
    def display_inventory(self):
        for item in self.list_items:
            if isinstance(item, Item):
                print(item.__dict__)
            else: 
                print(item)
        
    def add_item(self, item):
        for slot in range(len(self.list_items)):
            if self.list_items[slot] != 0:
                continue
            else: 
                self.list_items[slot] = item
                break