"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
resp ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
mais1k = barato = tot = 0
nome = ''
while True:
    prod = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: '))
    tot = tot + preco
    if barato == 0:
        barato = preco
        nome = prod
    if preco > 1000:
        mais1k += 1
    if preco < barato:
        barato = preco
        nome = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja resp? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'\n\033[34mTotal: R${tot:.2f}')
print(f'Quantidade de produtos que custam mais de 1k: {mais1k}')
print(f'O produto mais barato foi "{nome}", custando R${barato}\033[31m')
print('\nprograma finalizado\033[m')
