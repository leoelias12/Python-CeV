"""faça um programa que leia um numero de 0 a 9999 e mostre na tela cada digito separadamente
unidade, dezena, centena, milhar"""

num = int(input('Digite um numero inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O numero é {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))
