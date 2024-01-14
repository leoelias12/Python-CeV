"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randint
from time import sleep

npc = randint(0, 5)
print('Vou pensar em um número de 0 a 5, e vc adivinha!.')
print('PENSANDO...')
sleep(1)
numero = int(input('Pronto! pode adivinhar!\n'))

if numero == npc:
    print('Acertou mizeravi!!')
else:
    print('Errou, o número era {}.'.format(npc))
