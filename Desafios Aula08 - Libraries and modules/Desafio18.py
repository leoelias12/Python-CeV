'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math

ang = float(input("Digite o angulo desejado: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("Para um angulo de {} graus, o seno é {:.2f}, o cosseno {:.2f}, e a tangente {:.2f}.".format(ang, sen, cos, tan))
