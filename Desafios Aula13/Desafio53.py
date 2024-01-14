"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

frase = str(input('Digite uma frase:\n')).strip().upper()
lista = frase.split()
junto = (''.join(lista))
inverso = ''
#  aqui poderia colocar:
#  inverso == junto[::-1]
#  ao inves de usar o for
for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
#
#
#
print('===============')
if inverso == junto:
    print(f'Junto: {junto}')
    print(f'Inverso: {inverso}')
    print('É PALÍNDROMO')
else:
    print(f'Junto: {junto}')
    print(f'Inverso: {inverso}')
    print('NAO É PALÍNDROMO')

"""da pra fazer sem o uso de FOR dessa forma:
inverso == junto[::-1]
"""