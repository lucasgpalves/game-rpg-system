from models.items import Item

class Inventory:
    
    _slots = None
    _list_items = None
    
    def __init__(self, slots):
        self._slots = slots
        self._list_items = []
        
    def create_inventory(self):
        for slot in range(self._slots):
            self._list_items.append(0)
        
    def display_inventory(self):
        for item in self._list_items:
            if isinstance(item, Item):
                print(item.__dict__)
            else: 
                print(item)
        
    def add_item(self, item):
        for slot in range(len(self._list_items)):
            if self._list_items[slot] != 0:
                continue
            else: 
                self._list_items[slot] = item
                break