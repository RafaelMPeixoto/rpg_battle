import time


class Player:
    def __init__(self,vida, nome, ataque, defesa, equip):
        self.vida = vida
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.equip = equip

    def get_status(self):
        print(f'Seu jogador {self.nome} tem {self.vida} pontos de vida, força {self.ataque} de ataque, {self.defesa} de defesa e equipado com "{self.equip}"')

    def atacar(self, inimigo):
        print(f'Você está atacando com força {self.ataque} de ataque!')
        time.sleep(2)
        print(f'O inimigo tem {inimigo.vida} de vida!')
        time.sleep(2)
        inimigo.vida = inimigo.vida - self.ataque

        print(f'Após o ataque seu inimigo ficou com {inimigo.vida} pontos de vida!')

    