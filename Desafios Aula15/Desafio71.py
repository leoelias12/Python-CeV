"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
from time import sleep

print('{:=^40}'.format(' CAIXA ELETRÔNICO '))
valor = int(input('\nQuanto deseja sacar? '))
resto = valor
cinquenta = vinte = dez = um = 0
while True:
    while resto >= 50:
        cinquenta += 1
        resto -= 50
    while resto >= 20:
        vinte += 1
        resto -= 20
    while resto >= 10:
        dez += 1
        resto -= 10
    while resto >= 1:
        um += 1
        resto -= 1
    if resto == 0:
        break
print('{:=^40}'.format(' IMPRIMINDO '))
sleep(1)
print(f'\nNotas de R$50: {cinquenta}')
print(f'Notas de R$20: {vinte}')
print(f'Notas de R$10: {dez}')
print(f'Notas de R$01: {um}')

print('\n{:-^40}'.format(' SAQUE FINALIZADO '))
print('\n{:-^40}'.format(' RETIRE SEU DINHEIRO '))
