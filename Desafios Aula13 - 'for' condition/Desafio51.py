"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
print('\n\033[35mPROGRESSÃO ARITMÉTICA\033[m\n')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
q = pt + ((10 - 1) * r)
for c in range(pt, q + 1, r):
    print(c, end=' \033[31m🡆\033[m ')
print('FIM')

