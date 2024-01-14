"""Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""
matrix = [[], [], [], [], [], [], [], [], []]
n = 0
for c in range(0, 9):
    matrix[c].append(int(input('Digite um número: ')))
print(f'[{matrix[0:3]}]')
print(f'[{matrix[3:6]}]')
print(f'[{matrix[6:9]}]')
print()
print('FIM!')
