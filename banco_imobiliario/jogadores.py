from banco_imobiliario.propriedade import Propriedade


class JogadorBase():
    def __init__(self, saldo: int = 300) -> None:
        self.saldo = saldo
        self.posicao = 0
        
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