def display_menu():
    print(
        f'\n[1] - Movimentar'
        f'\n[2] - Atacar'
        f'\n[3] - Usar Item'
        f'\n[0] - Encerrar turno'
    )

rounds = 2

while True:
    
    display_menu()
    
    action = int(input("Selecione uma opção: "))
    
    if rounds == 0:
        print('Turno encerrado')
        break
    
    match action:
        case 0:
            print('Turno encerrado')
            break
    
        case 1:
            print("Movimentou")
            continue
        
        case 2:
            print("Atacou")
            rounds -= 1
            continue
        
        case 3:
            print("Usou um item")
            rounds -= 1
            continue