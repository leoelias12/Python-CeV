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


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
