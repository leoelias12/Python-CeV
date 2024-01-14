"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos."""

print('=' * 21)
print('\033[34mPROGRESSÃO ARITMÉTICA\033[m\n')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
c = 1
extra = 1
totterm = 10
while c < 10:
    print(f'{termo} → ', end='')
    termo = termo + r
    c = c + 1
print('FIM')
print('=' * 21)
while extra != 0:
    extra = int(input('\nQuantos termos extras vc gostaria de ver? '))
    c = 0
    totterm = totterm + extra
    while c < extra:
        print(f'{termo} → ', end='')
        termo = termo + r
        c = c + 1
        if c == extra:
            print('fim')
print('\n', '=' * 21)
print(f'\n\033[31mPROGRAMA FINALIZADO COM \033[34m{totterm}\033[31m termos mostrados')
