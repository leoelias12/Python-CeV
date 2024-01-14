"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""


def escreva(txt):
    tam = len(txt) + 4
    print(f"{'~' * tam}")
    print(f'  {txt}')
    print(f"{'~' * tam}")


msg1 = str(input('Digite uma mensagem: '))
msg2 = input('Digite outra mensagem: ')
msg3 = input('Digite mais uma mensagem: ')

escreva(msg1)
escreva(msg2)
escreva(msg3)