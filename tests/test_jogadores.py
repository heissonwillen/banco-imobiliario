import banco_imobiliario.jogadores as jogadores


def test_jogador_impulsivo():
    jogador = jogadores.JogadorImpulsivo(100)
    assert jogador.decide_compra(None)


def test_nome_jogador():
    jogador = jogadores.JogadorExigente(100)
    assert jogador.nome == 'Exigente'


def test_pagamento():
    jogador = jogadores.JogadorImpulsivo(100)
    jogador.paga(50)
    assert jogador.saldo == 50


def test_transferencia():
    jogador1 = jogadores.JogadorCauteloso(100)
    jogador2 = jogadores.JogadorExigente(100)
    jogador1.paga(50, jogador2)
    assert jogador1.saldo == 50
    assert jogador2.saldo == 150
