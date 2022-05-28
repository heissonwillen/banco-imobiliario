from matplotlib import pyplot as plt
import os
DIRETORIO_IMAGENS = 'imagens'


def salva_graficos(media_turnos: int, timeout: int, vencedores: dict, turnos: list):
    plt.axhline(y=media_turnos, color='r', linestyle='-', label='Média')
    plt.plot(turnos)
    plt.suptitle('Número de turnos por partida')
    plt.title(f'Partidas terminadas em timeout: {timeout}', fontsize=10)
    plt.xlabel('Partida')
    plt.ylabel('Turnos')
    plt.legend(loc='best')
    plt.savefig(os.path.join(DIRETORIO_IMAGENS,'num_turnos.png'))
    plt.close()

    plt.bar(list(vencedores.keys()), list(vencedores.values()))
    plt.title('Porcentagem de vitórias por jogador')
    plt.xlabel('Jogador')
    plt.ylabel('Porcentagem de vitórias')
    plt.savefig(os.path.join(DIRETORIO_IMAGENS,'porcentagem_vitorias.png'))
    plt.close()
