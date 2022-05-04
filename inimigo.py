from random import randint
import time

class Inimigo: 
    def __init__(self):
         self.nome = 'Dunga'
         self.ataque = randint(50,150)
         self.defesa = randint(10,50)
         self.vida = randint(200,400)  

    def get_status(self):
        print(f'Seu inimigo é {self.nome}, com {self.ataque} de ataque e {self.defesa} de defesa!')

    def contraAtaque(self, player):
        print(f'Você tem {player.vida} pontos de vida!')
        time.sleep(2)
        print(f'Seu inimigo contra-atacou, atacando com {self.ataque} de força de ataque!')
        time.sleep(2)
        player.vida = player.vida - self.ataque
        print(f'Após o contra-ataque seu player ficou com {player.vida} de vida!')
