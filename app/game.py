from models.entities import Player 
from models.items import Potion

jogador_1 = Player(30, 10, 4)
jogador_2 = Player(24, 14, 3)

attack = jogador_1.tackle(jogador_2)

print(f'Jogador 1 causou {attack} ao Jogador 2')
print(f'Jogador 2 \nVida atual : {jogador_2.health}')

potion = Potion(5, 'Poção de Vida', 10, 2)

heal = jogador_2.healing(potion)

print(f'Jogador 2 curou {heal} pontos de vida\nVida atual : {jogador_2.health}')

