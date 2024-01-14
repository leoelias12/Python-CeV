"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    escolha = int(input('Qual número de 0 a 10 deseja ver por extenso? [maior que 10 para parar]: '))
    if escolha > 10:
        break
    print('-' * 6)
    print(numeros[escolha])
    print('-' * 6)
print('=' * 19)
print('programa finalizado')