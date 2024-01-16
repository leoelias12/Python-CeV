"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[30;41m ERRO! Digite um número INTEIRO! \033[m')
        else:
            break
    print('-' * 30)
    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.'))
        except ValueError:
            print('\033[30;41m ERRO! Digite um número REAL! \033[m')
        else:
            break
    num = str(num).replace('.', ',')
    print('-' * 30)
    return num
