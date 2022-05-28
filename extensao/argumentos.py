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

parser.add_argument('--salvar-graficos',
                    action=argparse.BooleanOptionalAction,
                    dest='salvar_graficos',
                    default=False,
                    required=False,
                    help='Salva o gráfico da partida')

parser.add_argument('--imprimir-estatisticas',
                    action=argparse.BooleanOptionalAction,
                    dest='imprimir_estatisticas',
                    default=False,
                    required=False,
                    help='Imprime as estatísticas da partida')


argumentos = parser.parse_args()
