"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

lista = []
pares = []
impares = []
teste = ''
#  Criando a lista grupoipal
while True:
    lista.append(int(input('Digite um nUmero: ')))
    teste = str(input('Quer resp? [S/N] ')).upper()
    if 'N' in teste:
        break

#  separando pares e impares em 2 listas
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
    pos += 1

#  output
print('=' * 30)
print(f'lista: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
print('\n FIM')
