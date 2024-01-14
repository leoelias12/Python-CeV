"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
jogadores = {'P1': randint(1, 6), 'P2': randint(1, 6), 'P3': randint(1, 6), 'P4': randint(1, 6)}
print(f'{"==JOGANDO DADOS==":^30}')
for k, v in jogadores.items():
    print(f' - {k} tirou {v}')
    # sleep(1)

print()
ranking = dict(sorted(jogadores.items(), key=lambda x: x[1], reverse=True))

pos = 1
print(f'{"==RANKING DOS JOGADORES==":^30}')
for k, v in ranking.items():
    print(f'      {pos}ª lugar: {k} → {v}')
    pos += 1
