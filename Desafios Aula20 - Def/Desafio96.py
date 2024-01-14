"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""


def area(c, l):
    a = l * c
    print(f'{f"A área do terreno {l:.2f} x {c:.2f} é {a:.2f}m²":^45}')


def linha():
    print('=' * 45)


linha()
print(f'{"=======CALCULADORA DE ÁREA RETANGULAR========":^45}')
linha()
c = float(input('Digite o comprimento do terreno: '))
l = float(input('Digite a largura do terreno: '))
print()
linha()
area(l, c)
linha()
print(f'{"PROGRAMA ENCERRADO":^45}')