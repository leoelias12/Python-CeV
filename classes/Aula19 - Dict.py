  #         key      value       key    value  key   value
pessoas = {'nomes': 'Leonardo', 'sexo': 'M', 'idade': 26}
print(pessoas['nomes'], pessoas['sexo'], pessoas['idade'])

print(pessoas.keys())  # imprime as keys do dicionário
print(pessoas.values())  # imprime os valores do dicionário
print()
print(pessoas.items())
print()
for k in pessoas.keys():
    print({pessoas.values()})

for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
del pessoas['sexo']  # deleta a key 'sexo'
print(pessoas)

pessoas['nomes'] = 'Gustavo'  # altera o valor
pessoas['peso'] = 70  # adiciona uma key com value

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 100)
print()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['nome'] = str(input('Nome do estado: '))
    estado['sigla'] = str(input('Sigla do estado: ').upper())
    if c < 2:
        print('Próximo...')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()