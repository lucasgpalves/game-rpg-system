ACTIONS = 2
MAX_TURN = 4

def display_menu():
    print(
        f'\n[1] - Movimentar'
        f'\n[2] - Atacar'
        f'\n[3] - Usar Item'
        f'\n[0] - Encerrar turno'
    )

list_players = ['player_1', 'player_2', 'player_3', 'player_4']

turn = 0

# number_player = len(list_players)
# number_enemies = 2

# while number_player > 0 or number_player <= 0:
#     break


while turn < MAX_TURN: # alterar para True
    
    rounds = ACTIONS
    player_turn = list_players[0]

    print(player_turn.upper())

    while rounds > 0:
        
        print('-' * 10)
        
        display_menu()
        
        option = int(input("Selecione uma opção: "))
        
        if rounds == 0:
            print('Turno encerrado {player_turn}')
            break
        
        match option:
            case 0:
                print(f'Turno encerrado {player_turn}')
                break
        
            case 1:
                print(f'{player_turn} Movimentou') # player.move()
                rounds -= 1
                continue
            
            case 2:
                print(f'{player_turn} Atacou')
                rounds -= 1
                continue
            
            case 3:
                print(f'{player_turn} Usou um item')
                rounds -= 1
                continue
            
    list_players.pop(0)
    list_players.append(player_turn)
    turn += 1