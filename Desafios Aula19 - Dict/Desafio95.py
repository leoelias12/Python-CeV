"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
time = list()
jogador = dict()
partidas = list()
while True:
    partidas.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ').strip().title())
    jogador['partidas'] = int(input('Número de partidas jogadas: '))
    for c in range(1, jogador['partidas'] + 1):
        partidas.append(int(input(f'      Número de gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        print()
        resposta = str(input('Deseja incluir mais um jogador? [S/N] ').strip().upper())
        if resposta in 'SN':
            break
        print('ERRO! Por favor responda apenas com S ou N.')
    if resposta == 'N':
        break

print('=' * 45)
print(f'{"Cod":<3}  {"Nome":<15}{"Gols":<15}{"Total de gols"}')
for i, j in enumerate(time):
    print(f'|{i + 1:>3}  {j["nome"]:<15}{str(j["gols"]):<15}  {j["total de gols"]:>2}')
print('=' * 45)
while True:
    while True:
        print()
        resp = str(input('Deseja mostrar dados individuais? [S/N] ').strip().upper())
        if resp in 'SN':
            break
        print('ERRO! Por favor responda apenas com S ou N.')
    if resp in 'N':
        break
    elif resp == 'S':
        while True:
            seleciona = int(input('Digite o código do jogador desejado: '))
            if (seleciona - 1) >= len(time):
                print(f'ERRO! Não existe jogador com o número {seleciona}.')
            else:
                print()
                print('=' * 30)
                print(f'Levantamento do jogador {time[seleciona - 1]["nome"]}')
                for k, v in time[seleciona - 1].items():
                    if k == "gols":
                        for j, g in enumerate(v):
                            print(f'No jogo {j + 1} fez {g} gols')
                print('=' * 30)
                break

print()
print(f'{"===PROGRAMA ENCERRADO===":^30}')