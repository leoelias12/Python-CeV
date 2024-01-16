"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""
from numeros import leiaint, leiafloat
from textos import texto1, texto2

print('\033[7;48;30m', end='')
texto1('Função de leitura número inteiro e número real'), print('\033[m')
n1 = leiaint('\033[30;44mDigite um número INTEIRO:\033[m ')
n2 = leiafloat('\033[30;46mDigite um número REAL: \033[m')
print('-' * 30)
print(f'O valore inteiro digitado foi "{n1}" e o valor real foi "{n2}"')
