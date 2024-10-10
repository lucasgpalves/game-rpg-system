class Grid:
    _x = None
    _y = None
    _z = None 
    
    def __init__(self, x = 1, y = 1, z = 1):
        self._x = x
        self._y = y
        self._z = z
        self._table = []
        
    def create_grid(self):
        for layer in range(self._z):
            layer_list = []
            for column in range(self._y):
                row = [0] * self._x
                layer_list.append(row)
            self._table.append(layer_list)
            
    def display_grid(self):
        for layer in range(self._z):
            print(f'Layer {layer}')
            for column in range(self._y):
                print(f'Column {column}: {self._table[layer][column]}')
                
    def write_grid(self):
        return self._table