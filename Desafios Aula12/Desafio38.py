"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite um número\n'))
n2 = int(input('Digite outro número\n'))

if n1 > n2:
    print(f'O primeiro número ({n1}) é maior do que o segundo número ({n2})')

elif n1 == n2:
    print(f'Os valores {n1} e {n2} são iguais')
else:
    print(f'O segundo número ({n2}) é maior do que o primeiro número ({n1})')
