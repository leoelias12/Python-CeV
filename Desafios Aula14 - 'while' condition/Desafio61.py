"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""
print('\n\033[35mPROGRESSÃO ARITMÉTICA\033[m\n')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
c = 1
while c <= 10:
    print(f'{termo} → ', end='')
    termo += r
    c += 1
print('fim')