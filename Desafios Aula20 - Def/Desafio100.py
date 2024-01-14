"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
import random
from random import randint
num = list()


def sorteia(n):
    print('sorteando 5 valores...')
    for c in range(1, 6):
        num.append(randint(0, 10))
    print(f'Os valores sorteados foram: {num}')

def somapar(s):
    soma = 0
    print('Somando os valores pares:', end=' ')
    for n in num:
        if n % 2 == 0:
            print(n, end=' ')
            soma += n
    print(f'\nA soma dos números pares é: {soma}')

sorteia(num)
print()
somapar(list)
