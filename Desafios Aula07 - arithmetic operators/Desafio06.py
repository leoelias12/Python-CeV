"6 - crie um algoritmo que mostre o seu dobro, o seu triplo e a raiz quadrada"

n = int(input('Insira um número: '))
d = n*2
t = n*3
r = n**0.5

print('O dobro de {} é: {}'.format(n, d))
print('O triplo de {} é: {}'.format(n, t))
print('A raiz quadrada de {} é: {:.2f}'.format(n, r))
