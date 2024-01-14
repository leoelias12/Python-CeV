"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz demostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome='desconhecido', gols=0):
    """
    → Ficha de jogador de futebol
    :param nome: Nome no jogador (opcional)
    :param gols: Gols marcados pelo jogador (opcional)
    """
    print(f'O jogador {nome} marcou {gols} gol(s)')


n = str(input('Nome do jogador: ').strip().title())
g = str(input(f'Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)