def soma(a, b):  # Declarando 2 variaveis que serão preenchidas no uso
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é = {s}')


def contador(* n):  # armazena na variavel 'n' um número indefinido de valores com o uso do *
    s = sum(n)
    print(f'{len(n)} foram registrados')
    print(f'A soma dos {len(n)} números é de: {s}')


#  Main
soma(1, 4)
print()
soma(b=1, a=4)
print()
contador(4, 4, 2, 1, 3)
