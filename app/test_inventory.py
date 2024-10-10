from models import Inventory, Potion, Item

bag = Inventory(8)

bag.create_inventory()

potion = Potion(5, 'Poção de Vida', 10, 2)

bag.add_item(potion)

knife = Item('Faca', 10, 5)

bag.add_item(knife)

bag.display_inventory()

# bag = Inventory(27)

# bag.create_inventory()

# bag.display_inventory()

# chest = Inventory(54)

# bag.create_inventory()

# bag.display_inventory()