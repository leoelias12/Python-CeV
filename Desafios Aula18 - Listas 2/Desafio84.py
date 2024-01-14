"""Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoa = list()
grupo = list()
pesadas = leves = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    #  coloca valor em pesadas e leves se estover vazio
    if len(grupo) == 0:
        pesadas = pessoa[1]
        leves = pessoa[1]
    else:
        if pessoa[1] > pesadas:
            pesadas = pessoa[1]
        if pessoa[1] < leves:
            leves = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = input('Deseja resp? [S/N] ')
    if resp in 'Nn':
        break

print(15*'-')
print(f'{len(grupo)} pessoas foram cadastradas.\n', 15*'-')
print(f'O maior peso foi de: {pesadas}kg. Peso de: ', end='')
for p in grupo:
    if p[1] == pesadas:
        print(end=f'[{p[0]}]')
print()
print(f'O menor peso foi de: {leves}kg. Peso de: ', end='')
for p in grupo:
    if p[1] == leves:
        print(end=f'[{p[0]}]')
print('\n', 15*'-', '\nFIM!')
