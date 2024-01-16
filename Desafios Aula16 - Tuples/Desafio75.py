"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
par = ''
tup = (int(input('Digite um valor')),
       int(input('Digite outro valor')),
       int(input('Digite mais um valor')),
       int(input('Digite o último valor')))
print(tup)
print(f'O valor 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O primeiro valor 3 apareceu na posição {tup.index(3) + 1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')

