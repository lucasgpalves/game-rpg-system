from .item import Item
from .inventory import Inventory
from .player import Player

class Shop:
    
    def __init__(self, current_gold: float, storage: Inventory):
        self.current_gold = current_gold
        self.storage = storage
        
    def sell_item (self, player: Player, selled_item: Item):
        price_item = selled_item.price
        
        player_gold = player.inventory.get_gold()
        
        if player_gold < price_item:
            raise ValueError('You can\'t buy this item, you don\'t have enough gold')
        
        