from models import Player

jogador_1 = Player(30, 10, 4)
jogador_2 = Player(24, 14, 3)

attack = jogador_1.tackle(jogador_2)

print(f'Jogador 1 causou {attack} ao Jogador 2')
print(f'Jogador 2 \nVida atual : {jogador_2.health}')

