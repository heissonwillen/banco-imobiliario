import matplotlib.pyplot as plt
import banco_imobiliario.jogadores as jogadores
import banco_imobiliario.tabuleiro as tabuleiro
import argparse

parser = argparse.ArgumentParser(description='Jogo do Banco Imobiliário')
parser.add_argument('--limite-turnos',
                    action='store',
                    dest='limite_turnos',
                    type=int,
                    default=1000,
                    required=False,
                    help='Número limite de turnos por partida')

parser.add_argument('--bonus-rodada',
                    action='store',
                    dest='bonus_rodada',
                    type=int,
                    default=100,
                    required=False,
                    help='Valor do bônus por rodada para cada jogador')

parser.add_argument('--num-props',
                    action='store',
                    dest='num_props',
                    type=int,
                    default=20,
                    required=False,
                    help='Número de propriedades no tabuleiro')

parser.add_argument('--saldo-inicial',
                    action='store',
                    dest='saldo_inicial',
                    type=int,
                    default=300,
                    required=False,
                    help='Saldo de cada jogador no início da partida')

parser.add_argument('--num-partidas',
                    action='store',
                    dest='num_partidas',
                    type=int,
                    default=300,
                    required=False,
                    help='Número de partidas a serem simuladas')

arguments = parser.parse_args()


def cria_tabuleiro():
    return tabuleiro.Tabuleiro(
        jogadores=[jogadores.JogadorImpulsivo(saldo=arguments.saldo_inicial),
                   jogadores.JogadorExigente(saldo=arguments.saldo_inicial),
                   jogadores.JogadorCauteloso(saldo=arguments.saldo_inicial),
                   jogadores.JogadorAleatorio(saldo=arguments.saldo_inicial)],
        num_props=arguments.num_props,
        limite_turnos=arguments.limite_turnos,
        bonus_rodada=arguments.bonus_rodada)


res_jogos = [cria_tabuleiro().joga_partida()
             for _ in range(arguments.num_partidas)]
res_jogos.sort(key=lambda r: r["vencedor"])
turnos = [res.get("turno") for res in res_jogos]
timeout = len([res for res in res_jogos if res.get("timeout")])

vencedores = {}
for res in res_jogos:
    vencedor = res.get("vencedor")
    vencedores[vencedor] = vencedores.get(vencedor, 0) + 1

for k, v in vencedores.items():
    vencedores[k] = v / len(res_jogos) * 100

print(vencedores)

plt.bar(list(vencedores.keys()), list(vencedores.values()))
plt.show()

print(f"Média de turnos por partida {sum(turnos) / len(turnos)}")
print(f"Quantidade de partidas terminadas em timeout: {timeout}")
