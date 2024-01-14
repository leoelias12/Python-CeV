"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
 indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


def fatorial(n, show=True):
    """
    --> Calculo fatorial de um número.
    :param n: o número que será calculado o fatorial.
    :param show: True irá mostrar o cálculo completo
    :param show: False irá mostrar apenas o resultado
    """
    num = 1
    show = False
    for c in range(n, 0, -1):
        num *= c
    print(f'O resultado de {n}! é: \n>>>>>{num:^10}<<<<<')
    print('=' * 30)
    print()
    resp = input('Deseja mostrar o cáculo feito? ').upper().strip()

    if resp == 'S':
        show = True
    if show:
        for c in range(n, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
    return num


teste = int(input('Digite um número: '))
print('=' * 30)
print(fatorial(teste))
print('=' * 30)
print()

help(fatorial)
