list_players = ['player_1', 'player_2', 'player_3', 'player_4']

for i in range(10):
    this_round = list_players[0]
    
    list_players.pop(0) # remover itens da lista
    list_players.append(this_round) # adiciona no fim da lista
    
    print(f'Rodada do {this_round}')