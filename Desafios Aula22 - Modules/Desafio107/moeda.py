"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


def aumentar(n, porcentagem):
    """
    ==> Função que aumenta o número dado em determinada porcentagem desejada.
    :param n: Número inicial
    :param porcentagem: porcentagem que deseja acrescentar
    :return: retorna o número com acrecimo da porcentagem dada
    """
    x = n + (n * (porcentagem / 100))
    return f'{x:.2f}'


def diminuir(n, porcentagem):
    """
    ==> Função que subtrai a porcentagem desejada do valor dado
    :param n: Valor inicial
    :param porcentagem: Porcentagem desejada para subtrair
    :return: retorna o resultado de 'n - porcentagem'
    """
    x = n - (n * (porcentagem / 100))
    return f'{x:.2f}'


def dobro(n):
    """
    ==> Função para dobrar o valor dado
    :param n: Valor a ser dobrado
    :return: Retorna o valor * 2
    """
    x = n * 2
    return f'{x:.2f}'


def metade(n):
    """
    ==> Função para dizer a metade do valor dado
    :param n: Valor a ser calculado a metade
    :return: Retorna a metade do valor dado
    """
    x = n / 2
    return f'{x:.2f}'
