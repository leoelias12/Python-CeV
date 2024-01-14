"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(i, f, p):
    print('=' * 31)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f - 1, p * (-1)):
            print(c, end=' ')
            sleep(0.2)
        print('Fim')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.2)
        print('Fim!')


contador(1, 10, 1)
contador(10, 1, 1)
print()
print(f'{"===CONTAGEM PERSONALIZADA===":^31}')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('=' * 31)