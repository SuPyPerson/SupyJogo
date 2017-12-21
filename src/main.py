"""
O Jogo do Tesouro Inca de Pachamama
"""
from random import shuffle, randint
CIRCLE = 9311
TENDA = "\033[94m⛺\033[39m"


class Templo:
    """
    O conjunto de cartas que já foram apresentadas nesta rodada
    """
    def __init__(self, jogo):
        self.jogo = jogo
        self.templo = []

    def adentra(self, carta):
        self.jogo.apresenta_templo(self.templo+[carta])
        if carta in self.templo:
            self.jogo.eh_perigo()
        self.templo.append(carta)


class Baralho:
    """
    O conjunto de cartas que compõe o jogo
    """
    def __init__(self, jogo):
        self.jogo = jogo
        self.baralho = [carta for carta in range(1, 16)]
        self.baralho += [carta for carta in range(16, 21) for _ in range(0, 3)]
        shuffle(self.baralho)
        for carta in self.baralho:
            self.jogo.adentra(carta)
            if self.jogo.decide():
                break


class Jogador:
    """
    Um jogador Robo
    """
    TRUPE = []

    def __init__(self, templo, atento=70, medroso=40, incauto=30, ambicioso=60):
        self.templo, self.atento, self.medroso, self.incauto, self.ambicioso = \
            templo, atento, medroso, incauto, ambicioso
        Jogador.TRUPE.append(self)
        self.tesouro = 0

    def decide(self):
        meu = self

        def ambicioso():
            desejo = max(j.tesouro for j in Jogador.TRUPE)-meu.tesouro+self.ambicioso
            return desejo < randint(0, 100)

        def medroso():
            medo = sum(10 for carta in self.templo if carta in range(16, 21)) + self.medroso
            return medo < randint(0, 100)

        return all([ambicioso(), medroso()])


class Jogo:
    """
    O Jogo do Tesouro Inca
    """
    def __init__(self):
        self.mapa = {carta: "\033[92m"+chr(CIRCLE+carta)+"\033[39m" for carta in range(1, 16)}
        perigos = {p+16: "\033[31m{}\033[39m".format(face) for p, face in enumerate("🐍🔥🕷🧟🌋")}
        self.mapa.update(perigos)
        self.trupe = [Jogador(randint(20, 100),randint(20, 100),randint(20, 100),randint(20, 100))for _ in "abcd"]
        self.perigo = False
        self.templo = Templo(self)
        self.baralho = Baralho(self)

    def apresenta_acampamento(self):
        _ = self
        for jogador in self.trupe:
            print("{}:{:02}".format(TENDA, jogador.tesouro), end=" ")

    def apresenta_templo(self, templo):
        self.apresenta_acampamento()
        for carta in templo:
            self.apresenta_carta(carta)

    def apresenta_carta(self, carta):
        if carta in self.mapa:
            carta = self.mapa[carta]
        print(carta, end=" ")

    def decide(self):
        return self.perigo or (input("(s)sai ou (f)fica?") == "s")

    def adentra(self, carta):
        self.templo.adentra(carta)

    def eh_perigo(self,):
        self.perigo = True
        print("desatre, todos saem correndo!")


if __name__ == '__main__':
        Jogo()
