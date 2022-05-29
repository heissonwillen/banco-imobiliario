from extensao.graficos import salva_graficos
from extensao.estatisticas import obtem_estatisticas, imprime_estatisticas
from extensao.argumentos import argumentos
import banco_imobiliario.jogadores as jogadores
import banco_imobiliario.tabuleiro as tabuleiro
import random


def cria_tabuleiro():
    jogs = [jogadores.JogadorImpulsivo(saldo=argumentos.saldo_inicial),
            jogadores.JogadorExigente(saldo=argumentos.saldo_inicial),
            jogadores.JogadorCauteloso(saldo=argumentos.saldo_inicial),
            jogadores.JogadorAleatorio(saldo=argumentos.saldo_inicial)]

    return tabuleiro.Tabuleiro(
        jogadores=random.sample(jogs, len(jogs)),
        num_props=argumentos.num_props,
        limite_turnos=argumentos.limite_turnos,
        bonus_rodada=argumentos.bonus_rodada)


resultados = [cria_tabuleiro().joga_partida()
              for _ in range(argumentos.num_partidas)]

estatisticas = obtem_estatisticas(resultados)

if argumentos.salvar_graficos:
    salva_graficos(*estatisticas)

if argumentos.imprimir_estatisticas:
    imprime_estatisticas(*estatisticas)
