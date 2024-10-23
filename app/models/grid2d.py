from .item import Item

class Grid2D:
    
    def __init__(self, x: int, y: int, default_value: int = 0):
        self.x = x
        self.y = y
        self.table = self.create_grid(default_value)
        
    def create_grid(self, default_value):
        return [[default_value for _ in range(self.y)] for _ in range(self.x)]
            
    def display_grid(self):
            for column in range(self.y):
                print(f'Column {column}: {self.table[column]}')
                
    def write_grid(self):
        return self.table
    
    def add_object_in_grid(self, obj, cords):
        x, y = self.attribute_cords(cords)
        if self.table[x][y] == 0:
            self.table[x][y] = obj
        else:
            new_cords = self.increment_cords((x, y))
            self.add_object_in_grid(obj, new_cords)
        
        
    def attribute_cords(self, cords):
        return cords.x, cords.y
    
    def increment_cords(self, cords):
        x, y = cords
        
        return (x + 1, y)
    
    def create_item(self, cords, item: Item):
        if item is None:
            raise ValueError(f'This item {item} don\'t exists')
        
        x, y = self.attribute_cords(cords)
        
        if y >= len(self.table) or x >= len(self.table[0]):
            raise IndexError('Coordinates out of bounds')
        
        for dy in range(y):
            for dx in range(x):
                self.table[dy][dx] = item
        
        
    
    def destroy_item(self, cords, item: Item):
        x, y = self.attribute_cords(cords)
        
        if item.destroy():
            # Finalizar a implementação deste método
            self.table[x][y] = 0
        
        
        
        