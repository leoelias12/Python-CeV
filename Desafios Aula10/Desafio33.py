"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
n1 = int(input('Digite o primeiro numero.\n'))
n2 = int(input('Digite o segundo numero.\n'))
n3 = int(input('Digite o terceiro numero\n'))

#  testando o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#  testando maio número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}'.format(menor))
print('O maio número é {}'.format(maior))
