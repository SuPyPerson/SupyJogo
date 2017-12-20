"""
Módulo principal do Jogo Inca.
"""
from random import shuffle
CIRCLE = 9311



class Baralho:
    '''
    Contém todas as cartas do jogo.
    '''

    def __init__(self,jogo):
        self.jogo = jogo
        self.baralho = [carta for carta in range(1, 16)]
        self.baralho += [carta*3 for carta in range(16, 21)]
        shuffle(self.baralho)
        for carta in self.baralho:
            self.jogo.apresenta_carta(carta)
            if self.jogo.decide():
                break



class Carta:
    """
    Representa Artefatos, Tesouro ou Perigo.
    """
    ...


class Tunel:
    '''
    Parte interna do templo onde se encontra coisas boas ou más.
    '''

    ...

class Jogo:
    '''
    O Jogo Principal.
    '''
    def __init__(self):
        self.mapa = {carta: "\033[92m"+chr(CIRCLE+carta)+ "\033[39m" for carta in range (1, 16)}
        self.mapa[16] = self.mapa[17] = self.mapa[18] = "\033[31m🐍\033[39m"
        self.mapa[19] = self.mapa[20] = self.mapa[21] = "\033[31m🕷\033[39m"
        self.mapa[22] = self.mapa[23] = self.mapa[24] = "\033[31m🔥\033[39m"
        self.mapa[25] = self.mapa[26] = self.mapa[27] = "\033[31m🧟\033[39m"
        self.mapa[28] = self.mapa[29] = self.mapa[30] = "\033[31m🐁\033[39m"

        self.baralho = Baralho(self)
        print('Bem vindo ao misterioso Templo Inca')


    def apresenta_carta(self, carta):
        if carta in self.mapa:
           carta = self.mapa[carta]
        print(carta, end=" ")

    def decide(self):
        escolha = input("(s)sai ou (f)fica?")
        return escolha == "s"




if __name__== '__main__':
    Jogo()