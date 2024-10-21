from .player import Player

class Hud:
    
    def __init__(self, player: Player):
        self.player = player
        
    def display_hud(self):
        print(
            f'Name: {self.player.name} '
            f'HP: {self.player.health}/{self.player.max_health} '
            f'Level: {self.player.level} XP: {self.player.xp}'
        )