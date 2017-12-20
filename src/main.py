"""
O Jogo do Tesouro Inca de Pachamama
"""
from random import shuffle
CIRCLE = 9311


class Baralho:
    """
    O conjunto de cartas que compõe o jogo
    """
    def __init__(self, jogo):
        self.jogo = jogo
        self.baralho = [carta for carta in range(1, 16)]
        self.baralho += [carta*3 for carta in range(16, 21)]
        shuffle(self.baralho)
        for carta in self.baralho:
            self.jogo.apresenta_carta(carta)
            if self.jogo.decide():
                break


class Jogo:
    """
    O Jogo do Tesouro Inca
    """
    def __init__(self):
        self.mapa = {carta: "\033[92m"+chr(CIRCLE+carta)+"\033[39m" for carta in range(1, 16)}
        self.mapa[16] = self.mapa[16] = self.mapa[16] = "\033[31m🐍\033[39m"
        self.mapa[17] = self.mapa[17] = self.mapa[17] = "\033[31m🔥\033[39m"
        self.mapa[18] = self.mapa[18] = self.mapa[18] = "\033[31m🕷️\033[39m"
        self.mapa[19] = self.mapa[19] = self.mapa[19] = "\033[31m🧟\033[39m"
        self.mapa[10] = self.mapa[20] = self.mapa[20] = "\033[31m🌋\033[39m"
        self.baralho = Baralho(self)

    def apresenta_carta(self, carta):
        if carta in self.mapa:
            carta = self.mapa[carta]
        print(carta, end=" ")

    @staticmethod
    def decide():
        escolha = input("(s)sai ou (f)fica?")
        return escolha == "s"


if __name__ == '__main__':
        Jogo()
