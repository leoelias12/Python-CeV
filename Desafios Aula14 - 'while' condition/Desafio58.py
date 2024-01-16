"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
pc = randint(1, 10)
c = 1
print('=' * 25, '\n')
print('vou pensar em um número de 1 a 10 e vc adivinha!')
print('PENSANDO...')
sleep(2)
print('Pronto, pode adivinhar.\n')
print('=' * 25)

guess = int(input('Digite um número: '))

while guess != pc:
    guess = int(input('Errou! Tenta de novo.\nDigite outro número: '))
    c = c + 1
print(f'\nACERTOU MIZERAVI! Era o número {pc}.')
print(f'Vc precisou de {c} tentativas para acertar.')
