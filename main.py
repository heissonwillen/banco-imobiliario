import matplotlib.pyplot as plt
import banco_imobiliario.jogadores as jogadores
import banco_imobiliario.tabuleiro as tabuleiro


def cria_tabuleiro():
    return tabuleiro.Tabuleiro(jogadores=[jogadores.JogadorImpulsivo(),
                                          jogadores.JogadorExigente(),
                                          jogadores.JogadorCauteloso(),
                                          jogadores.JogadorAleatorio()])


res_jogos = [cria_tabuleiro().joga_partida() for _ in range(300)]
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
