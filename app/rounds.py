"""
Existem jeitos melhores de se realizar alguns processos, porém o importante vai ser o resultado

list_players = ['player_1', 'player_2', 'player_3', 'player_4']

for i in range(10):
    this_round = list_players[0]
    
    list_players.pop(0) # remover itens da lista
    list_players.append(this_round) # adiciona no fim da lista
    
    print(f'Rodada do {this_round}')

"""

from collections import deque

players = deque(['player_1', 'player_2', 'player_3', 'player_4'])

for round_number in range(1, 11):
    current_player = players[0]
    players.rotate(-1)
    
    print(f'Rodada {round_number}, sua vez {current_player}')