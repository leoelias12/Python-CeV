"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


def aumentar(n, porcentagem, formato=False):
    x = n + (n * (porcentagem / 100))
    return x if formato is False else moeda(x)


def diminuir(n, porcentagem, formato=False):
    x = n - (n * (porcentagem / 100))
    return x if formato is False else moeda(x)


def dobro(n, formato=False):
    x = n * 2
    return x if formato is False else moeda(x)


def metade(n, formato=False):
    x = n / 2
    return x if formato is False else moeda(x)


def moeda(n=0, currency='R$'):
    return f'{currency:<3}{n:>7.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, reduc=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Valor analisado:":<20}{moeda(n):>8}')
    print(f'{f"{aumento:.0f}% de aumento:":<20}{aumentar(n, aumento, True):>8}')
    print(f'{f"{reduc:.0f}% de redução:":<20}{diminuir(n, reduc, True):>8}')
    print(f'{"Dobro do valor:":<20}{dobro(n, True):>8}')
    print(f'{"Metade do valor:":<20}{metade(n, True):>8}')
    print('-' * 30)
