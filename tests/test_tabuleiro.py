import banco_imobiliario.jogadores as jogadores
import banco_imobiliario.tabuleiro as tabuleiro
import pytest


def test_jogador_impulsivo():
    t = tabuleiro.Tabuleiro(
        jogadores=[jogadores.JogadorImpulsivo(100),
                   jogadores.JogadorExigente(100),
                   jogadores.JogadorCauteloso(100),
                   jogadores.JogadorAleatorio(100)])

    jogador = jogadores.JogadorImpulsivo(100)
    propriedade = t.props[0]
    assert jogador.decide_compra(propriedade)


def test_tabuleiro_sem_jogadores():
    t = tabuleiro.Tabuleiro()
    assert t.jogadores == []


def test_remove_jogador():
    jog = jogadores.JogadorImpulsivo()
    tab = tabuleiro.Tabuleiro([jog])
    tab.remove_jogador(jog)
    assert tab.jogadores == []


def test_remove_jogador2():
    tab = tabuleiro.Tabuleiro(
        [jogadores.JogadorImpulsivo(), jogadores.JogadorImpulsivo()])
    jogador_para_remover = tab.jogadores[0]
    tab.remove_jogador(jogador_para_remover)
    assert len(tab.jogadores) == 1


def test_remove_jogador_inexistente():
    jogador = jogadores.JogadorImpulsivo()
    tab = tabuleiro.Tabuleiro([jogador])
    jogador_inexistente = jogadores.JogadorImpulsivo()
    with pytest.raises(ValueError):
        tab.remove_jogador(jogador_inexistente)


def test_quantidade_proprietarios():
    tab = tabuleiro.Tabuleiro(num_props=30)
    assert len(tab.props) == 30
