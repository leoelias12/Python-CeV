"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o
maior."""
from time import sleep


def maior(* num):
    v = 0
    print('Analisando os valores passados...')
    for i, n in enumerate(num):
        if i == 0:
            v = n
        else:
            if n > v:
                v = n
        print(n, end=' ')
    print()
    print(f'O maior valor encontrado foi: {v}')
    print('=' * 30)

maior(5, 7, 4 ,84 ,56 ,48 ,26, 98 ,74)
print()
maior(3, 6, 7)