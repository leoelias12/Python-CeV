"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""


def leiaint(i):
    while True:
        inte = str(input(i).strip())
        if not inte.isnumeric():
            print('ERRO. DIGITE UM NÚMERO INTERIO VÁLIDO.')
        else:
            break
    return inte


n = leiaint('Digite um número: ')
print(f'Vc digitou {n}')