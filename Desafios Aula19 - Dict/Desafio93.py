"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador = dict()
n = 1
totgols = 0
jogador['nome'] = str(input('Nome do jogador: ').strip().title())
jogador['partidas'] = int(input('Número de partidas jogadas: '))
for c in range(1, jogador['partidas'] + 1):
    jogador[f'partida {n}'] = int(input(f'Número de gols na partida {n}: '))
    totgols += jogador[f'partida {n}']
    n += 1
jogador['total de gols'] = totgols
print('=' * 30)
print(f'O jogador {jogador["nome"].title()} jogou {jogador["partidas"]} partidas')
for k, v in jogador.items():
    if k != 'nome' and k != 'partidas' and k != 'total de gols':
        print(f'    => Na {k}, marcou {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')
