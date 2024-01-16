"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

fat = int(input('Digite o número desejado: '))
c = fat
result = 1
print(f'Calculando {fat}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    result = result * c
    c = c - 1
print(result)
