from random import randint
import time
from player import Player
from inimigo import Inimigo

vida = 100
nome="Goku"
ataque=100
defesa=1000
equip="Bastão"

player = Player(vida, nome, ataque, defesa, equip)
inimigo = Inimigo()

# player.get_status()
# inimigo.get_status()
# player.atacar(inimigo)
# print('____________________________________________________Contra-ataque____________________________________________________')
# time.sleep(2)
# inimigo.contraAtaque(player)


# print(f'Seu jogador é {nome}, com {ataque} de ataque, {defesa} de defesa e equipado com "{equip}"')
# print(f'Ataque:{ataque}')
# print(f'Defesa:{defesa}')
# print(f'Equipamento: {equip}')

turno = randint(1,2)


jogo_rolando = True
while jogo_rolando:
    print("Jogo rolando!")

    if turno == 1:
        player.atacar(inimigo)
        turno = 2
    elif turno == 2:
        inimigo.contraAtaque(player)
        turno = 1
    
    


    
        
    
    

    





