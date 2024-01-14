"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint

l = 0
w = 0
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    pc = randint(0, 10)
    player = int(input('Escolha um número de 0 a 10: '))
    tot = pc + player
    print(f'\nPC: {pc}\nJogador: {player}\nTotal: {tot}')
    if tot % 2 == 0 and escolha == 'P':
        print('Você ganhou! Vamos de novo!')
        w = w + 1
    elif tot % 2 != 0 and escolha == 'I':
        print('Você ganhou! Vamos de novo!')
        w = w + 1
    elif tot % 2 == 0 and escolha == 'I':
        print('Vc perdeu!')
        l = l + 1
        break
    elif tot % 2 != 0 and escolha == 'P':
        print('Vc perdeu!')
        l = l + 1
        break
print(f'Total de vitórias consecutivas: {w}')
print('GG WP')