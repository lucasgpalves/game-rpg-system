from models import Potion, Player

potion = Potion(5, 'Poção de Vida', 10, 2)
jogador_2 = Player(24, 14, 3)

potion.to_string()

jogador_2.healing(potion)

potion.to_string()