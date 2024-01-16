"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
somatot entre elas (desconsiderando o flag)."""

s = 0
c = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'\nA somatot dos {c} valores digitados é de {s}')