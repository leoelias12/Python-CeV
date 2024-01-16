"""Faça um programa que calcule a somatot entre todos os números que são múltiplos de três e
que se encontram no intervalo de 1 até 500."""
import math
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'a somatot dos {cont} valores solicitados é de {s}.')