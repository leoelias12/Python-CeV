"""Desenvolva um programa que leia o comprimento de três retas e
 diga ao usuário se elas podem ou não formar um triângulo."""

r1 = int(input('Tamanho da reta 1\n'))
r2 = int(input('Tamanho da reta 2\n'))
r3 = int(input('Tamanho da reta 3\n'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode')
else:
    print('Não pode')
