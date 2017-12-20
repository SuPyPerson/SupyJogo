"""
modulo principal do jogo inca
"""
from random import shuffle
CIRCLE=9311


class Carta:
    """
    contém artefato, perigo ou tesouro.
    """


class Baralho:
    """
    conjunto de cartas que compõem o jogo
    """
    def __init__(self, jogo):
        self.jogo = jogo
        self.baralho = [carta for carta in range(1, 16)]
        self.baralho += [carta*3 for carta in range(16, 21)]
        shuffle(self.baralho)
        for carta in self.baralho:
            self.jogo.apresenta__carta(carta)
            if self.jogo.decide():
             break

class Jogo:
    """
    o jogo do tesouro inca
    """
    def __init__(self):
        self.mapa = {carta: "\033[92m"+chr(CIRCLE+carta)+"\033[39"for carta in range(1, 16)}
        self.mapa[16] ="\033[31m🐍\033[39m"
        self.mapa[17] ="\033[31m🕷️\033[39m"
        self.mapa[18] ="\033[31m🔥\033[39m"
        self.mapa[19] ="\033[31m🧟\033[39m"
        self.mapa[20] ="\033[31m🗻\033[39m"

        self.baralho = Baralho(self)

    def apresenta__carta(self, carta):
        if carta in self.mapa:
           carta = self.mapa[carta]
        print(carta, end=" ")

    def decide(self):
            escolha = input("(s)sai ou (f)fica?")
            return escolha == "s"


if __name__ == "__main__":
    Jogo()


