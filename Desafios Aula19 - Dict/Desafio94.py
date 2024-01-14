"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
lista = list()
totidade = 0
mulheres = list()
n = 1
while True:
    pessoa = {'nome': '', 'sexo': ' ', 'idade': 0}
    pessoa['nome'] = str(input('Nome: ').strip().title())
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ').strip().upper())
        if pessoa['sexo'] not in 'MF':
            print('Sexo inválido! Tente novamente.')
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    totidade += pessoa['idade']
    media = totidade / len(lista)
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ').upper().strip())
        if continua not in 'SN':
            print('Opção inválida!')
    if continua == 'N':
        break

print('=' * 30)
print()
print(f'A) Número de pessoas cadastradas: {len(lista)}.')
print(f'B) Média de idade: {media:.2f}')
print(f'C) Mulheres cadastradas: ')
for c in mulheres:
    print(f' - {c}')
print(f'D) Pessoas acima da média de idade:')
for c in lista:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'    {k} = {v};', end='')
            if k == 'idade':
                print()
