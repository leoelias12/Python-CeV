"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Atletico-PR', 'Fortaleza',
         'Atlétigo-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
         'Vasco', 'América-MG', 'Coritiba')

print('OS 5 PRIMEIROS COLOCADOS SÃO:\n'
      '1 - ', times[0],
      '\n2 - ', times[1],
      '\n3 - ', times[2],
      '\n4 - ', times[3],
      '\n5 - ', times[4])
print('=' * 15)
print('\nOS 4 ÚLTIMOS COLOCADOS SÃO:'
      '\n17 - ', times[16],
      '\n18 - ', times[17],
      '\n19 - ', times[18],
      '\n20 - ', times[19])
print('=' * 15)
print('TIMES EM ORDEM ALFABÉTICA\n', sorted(times))
print('=' * 15)
print(f'cruzeiro está na posição {times.index("Cruzeiro")+1}')