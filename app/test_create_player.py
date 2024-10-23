from models import Player, Inventory

inventory = Inventory(slots=8)

player_1 = Player(name="Thoryn", health=120, max_health=120, armor=17, movement=6, level=5, xp=1300, inventory=inventory)

print(player_1.__dict__)

player_1._inventory.create_inventory()
player_1._inventory.display_inventory()