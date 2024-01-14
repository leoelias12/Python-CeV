"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os
valores pares e ímpares em ordem crescente."""
n = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        n[1].append(valor)
    else:
        n[0].append(valor)
n[0].sort()
n[1].sort()
print(n)
