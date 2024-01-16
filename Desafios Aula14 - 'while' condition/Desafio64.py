"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a somatot entre eles (desconsiderando o flag)."""

s = 0
c = 0
n = 0
print('=' * 42)
while n != 999:
    n = int(input('\nDigite um número inteiro [999 para parar]: '))
    if n != 999:
        s = s + n
        c = c + 1
print(f'\nVc inseriu um total de {c} números.')
print(f'A somatot entre todos os números inseridos é: {s}')
print(f'\nPROGRAMA ENCERRADO')
