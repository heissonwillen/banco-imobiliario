import random


class Propriedade():
    def __init__(self, posicao: int) -> None:
        self.custo_venda = random.randint(30, 90)
        self.valor_aluguel = random.randint(10, 60)
        self.posicao = posicao
        self.dono = None
