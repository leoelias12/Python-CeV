"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa
se encerrará. Importante: use cores."""
from time import sleep

color = ('\033[m',  # 0 - Default color
         '\033[0;30;41m',  # 1 - Red
         '\033[0;30;42m',  # 2 - Green
         '\033[0;30;43m',  # 3 - Yellow
         '\033[0;30;44m',  # 4 - Blue
         '\033[0;30;45m',  # 5 - Purple
         '\033[7m'  # 6 - Branco
         )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(color[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(color[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(color[6], end='')
    help(com)
    print(color[0], end='')
    sleep(2)


# Main
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca: ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('Pograma Finalizado', 1)