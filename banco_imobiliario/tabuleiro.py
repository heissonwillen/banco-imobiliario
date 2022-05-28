import random
from banco_imobiliario.jogadores import JogadorBase
from banco_imobiliario.propriedade import Propriedade


class Tabuleiro():
    def __init__(self,
                 jogadores: list[JogadorBase] = [],
                 num_props: int = 20,
                 limite_turnos: int = 1000,
                 bonus_rodada: int = 100) -> None:
        self.num_props = num_props
        self.props = [Propriedade(i) for i in range(self.num_props)]
        self.jogadores = jogadores
        self.turno = 0
        self.vencedor = None
        self.limite_turnos = limite_turnos
        self.bonus_rodada = bonus_rodada

    @property
    def joga_dado(self) -> int:
        return random.randint(1, 6)

    def __dict__(self) -> dict:
        return {
            "turno": self.turno,
            "vencedor": self.vencedor.nome,
            "timeout": self.turno == self.limite_turnos,
        }

    def remove_jogador(self, jogador: JogadorBase) -> None:
        for prop in self.props:
            if prop.dono == jogador:
                prop.dono = None
        self.jogadores.remove(jogador)

    def verifica_fim_de_jogo(self) -> None:
        if len(self.jogadores) == 1:
            self.vencedor = self.jogadores[0]
        elif self.turno == self.limite_turnos:
            self.vencedor = max(self.jogadores, key=lambda j: j.saldo)

    def joga_rodada(self) -> None:
        for jogador in self.jogadores:
            self.verifica_fim_de_jogo()
            if self.vencedor:
                return

            nova_posicao = jogador.posicao + self.joga_dado
            if nova_posicao >= self.num_props:
                jogador.saldo += self.bonus_rodada
                nova_posicao -= self.num_props

            jogador.posicao = nova_posicao
            jogador.interage_com_propriedade(self.props[jogador.posicao])

            if jogador.saldo < 0:
                self.remove_jogador(jogador)

    def joga_partida(self) -> dict:
        while True:
            self.joga_rodada()
            if self.vencedor:
                break
            self.turno += 1

        return self.__dict__()
