"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

r1 = int(input('Tamanho da reta 1.\n'))
r2 = int(input('Tamanho da reta 2.\n'))
r3 = int(input('Tamanho da reta 3.\n'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('É possivel montar um triângulo EQUILÁTERO com as retas fornecidas')
    elif (r1 == r2 != r3) or (r2 == r3 != r1):
        print('É possivel montar um triângulo ISÓCELES com as retas fornecidas.')
    else:
        print('É possivel montar um triângulo ESCALENO com as retas fornecidas.')
else:
    print('Não é possivel formar um triangulo com os tamanhos de retas fornecidos.')
    