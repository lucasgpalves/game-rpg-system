from models import Hud, Player, Inventory

inventory = Inventory(slots=8)

player_1 = Player(name="Thoryn", health=120, max_health=120, armor=17, movement=6, level=5, xp=1300, inventory=inventory)

hud = Hud(player = player_1)

hud.display_hud()