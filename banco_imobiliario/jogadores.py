import random
from banco_imobiliario.propriedade import Propriedade


class JogadorBase():
    def __init__(self, saldo: int = 300) -> None:
        self.saldo = saldo
        self.posicao = 0

    @property
    def nome(self) -> str:
        return self.__class__.__name__.replace("Jogador", "")

    def interage_com_propriedade(self, prop: Propriedade) -> None:
        if prop.dono and prop.dono != self:
            self.paga(prop.valor_aluguel, prop.dono)
        else:
            if self.decide_compra(prop):
                self.paga(prop.custo_venda)
                prop.dono = self

    @classmethod
    def decide_compra(self, prop: Propriedade) -> bool:
        raise NotImplementedError

    def paga(self, valor, dono=None) -> None:
        self.saldo -= valor
        if dono:
            dono.saldo += valor


class JogadorImpulsivo(JogadorBase):
    def decide_compra(self, prop: Propriedade) -> bool:
        return True


class JogadorExigente(JogadorBase):
    def decide_compra(self, prop: Propriedade) -> bool:
        return prop.valor_aluguel > 50


class JogadorCauteloso(JogadorBase):
    def decide_compra(self, prop: Propriedade) -> bool:
        return self.saldo - prop.custo_venda > 80


class JogadorAleatorio(JogadorBase):
    def decide_compra(self, prop: Propriedade) -> bool:
        return random.choice([True, False])
