"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores."""
from datetime import date
maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da pessoa {c + 1}: '))
    idade = date.today().year - ano
    if idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1

print('\n', '=' * 41, '\n')
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade')
