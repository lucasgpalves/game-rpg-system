from .item import Item
from .player import Player
from typing import List

class Quest:
    
    def __init__(self, title: str, xp: int = 0, is_completed:bool = False, rewards: List[Item] = None):
        self.title = title
        self.xp = xp
        self.is_completed = is_completed
        self.rewards = rewards if rewards else []
        
    def complete_quest(self, player: Player):
        self.give_reward(player)
        self.give_xp(player)
        self.is_completed = True
        
    def show_quest(self):
        return f"Title: {self.title} \nReward: {self.rewards} \nIs Completed: {self.is_completed}"
    
    def give_reward(self, player: Player):
        for reward in self.rewards:
            player.inventory.add_item(reward)
            
    def give_xp(self, player: Player):
        player.xp += self.xp