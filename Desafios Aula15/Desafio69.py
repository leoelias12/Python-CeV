"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não resp. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
me18 = 0
h = 0
mulmenor = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA pessoa'.center(30))
    print('-' * 30)
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo in 'H':
        h += 1
    if idade < 18:
        me18 += 1
    if idade < 20 and sexo in 'M':
        mulmenor += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja resp? [S/N]: ')).upper().strip()
    if escolha == 'N':
        break
print('\n')
print('=' * 30)
print(f'pessoas menores de 18 anos: {me18}')
print(f'Número de homens: {h}')
print(f'Mulheres com menos de 20 anos: {mulmenor}')
print('=' * 30)
print('\nPROGRAMA FINALIZADO')