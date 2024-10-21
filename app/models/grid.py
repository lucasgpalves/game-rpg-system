from models import Item

class Grid:
    
    def __init__(self, x: int, y: int, z: int, default_value: int = 0):
        self.x = x
        self.y = y
        self.z = z
        self.table = self.create_grid(default_value)
        
    def create_grid(self, default_value):
        return [[[default_value for _ in range(self.x)] for _ in range(self.y)] for _ in range(self.z)]
            
    def display_grid(self):
        for layer in range(self.z):
            print(f'Layer {layer}')
            for column in range(self.y):
                print(f'Column {column}: {self.table[layer][column]}')
                
    def write_grid(self):
        return self.table
    
    def add_object_in_grid(self, obj, cords):
        x, y, z = self.attribute_cords(cords)
        if self.table[x][y][z] == 0:
            self.table[x][y][z] = obj
        else:
            new_cords = self.increment_cords((x, y, z))
            self.add_object_in_grid(obj, new_cords)
        
        
    def attribute_cords(self, cords):
        return cords.x, cords.y, cords.z
    
    def increment_cords(self, cords):
        x, y, z = cords
        
        return (x + 1, y, z)
    
    def destroy_item(self, cords, item: Item):
        x, y, z = self.attribute_cords(cords)
        
        if item.destroy():
            # Finalizar a implementação deste método
            self.table[x][y][z] = 0
        
        
        
        