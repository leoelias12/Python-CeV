"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci."""
print('\033[34m=' * 30)
print(' ' * 3, 'SEQUÊNCIA DE FIBONACCI')
print('=' * 30)
n = int(input('\033[m\nDigite o número de elementos desejados: '))
n1 = 0
n2 = 1
c = 3
print(f'{n1} → {n2} → ', end='')
while c < n:
    n3 = n1 + n2
    print(f'{n3} → ', end='')
    n1 = n2
    n2 = n3
    c += 1
print('FIM\n')
print('\033[34m=' * 30)
