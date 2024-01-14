"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input(f'Digite o peso da pessoa {c + 1}: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('\n', '=' * 27, '\n')
print(f'O maior peso foi {maior:.2f}.')
print(f'O menor peso foi {menor:.2f}')
