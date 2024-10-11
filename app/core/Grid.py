class Grid:
    
    def __init__(self, x = 1, y = 1, z = 1, default_value = 0):
        self.x = x
        self.y = y
        self.z = z
        self.table = self.create_grid(default_value)
        
    def create_grid(self, default_value):
        for layer in range(self.z):
            layer_list = []
            for column in range(self.y):
                row = [default_value] * self.x
                layer_list.append(row)
            self.table.append(layer_list)
            
    def display_grid(self):
        for layer in range(self.z):
            print(f'Layer {layer}')
            for column in range(self.y):
                print(f'Column {column}: {self.table[layer][column]}')
                
    def write_grid(self):
        return self.table