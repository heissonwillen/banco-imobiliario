def obtem_estatisticas(resultados: list[dict]):
    resultados.sort(key=lambda r: r["vencedor"])
    turnos = [res.get("turno") for res in resultados]
    quantidade_timeouts = len(
        [res for res in resultados if res.get("timeout")])
    media_turnos = sum(turnos) / len(turnos)

    vencedores = {}
    for res in resultados:
        vencedor = res.get("vencedor")
        vencedores[vencedor] = vencedores.get(vencedor, 0) + 1

    for k, v in vencedores.items():
        vencedores[k] = v / len(resultados) * 100

    return media_turnos, quantidade_timeouts, vencedores, turnos


def imprime_estatisticas(media_turnos: int,
                         quantidade_timeout: int,
                         vencedores: dict, turnos: list):
    print(f"Média de turnos por partida: {media_turnos:.2f}")
    print(f"Partidas terminadas em timeout: {quantidade_timeout}")
    print(f"Jogador com mais vitórias: \
{max(vencedores, key=lambda k: vencedores[k])}")
    print("Porcentagem de vitórias por jogador:")
    for k, v in vencedores.items():
        print(f" - {k}: {v:.2f}%")
