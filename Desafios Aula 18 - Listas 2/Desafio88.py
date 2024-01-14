"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""
from random import randint
text = 'GERADOR DE JOGOS DA MEGA-SENA'
jogo = list()
composta = list()
print('=' * 40)
print(f'{text:^40}')
print('=' * 40)
qtd = int(input('Quantos jogos deseja fazer? '))
for c in range(1, qtd+1):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    composta.append(jogo[:])
    jogo.clear()
for n, j in enumerate(composta):
    print(f'jogo {n+1}:', f'{j}')
print()
print('BOA SORTE!')
