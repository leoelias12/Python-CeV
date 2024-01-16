"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla."""
from random import randint

tup = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Números gerados: {tup}')
print(f'o menor valor é: {min(tup)}')
print(f'o maior valor é: {max(tup)}')
