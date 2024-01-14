"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []

while True:
    n = (int(input('Digite um valor[0 para parar]: ')))
    if n == 0:
        break
    lista.append(n)

print('=' * 30)
print(f'\nLista criada: {lista}')
print(f'Quantidade de valores digitados: {len(lista)}')
print(f'Lista em ordem crescente: {sorted(lista, reverse = True)}')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print(f'O número 5 nao está na lista.')
