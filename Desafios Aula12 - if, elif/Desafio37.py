"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

n = int(input('Digite na base DECIMAL o número que deseja converter.\n'))
base = int(input('Digite o número referente a base da qual deseja converter. '
                 '\nBinário (1)\nHexadecimal (2)\nOctal (3)\n'))

if base == 1:
    print(f'O número {n} convertido para binário é: {bin(n) [2:]}')
elif base == 2:
    print(f'O número {n} na base hexadecimal é: {hex(n).upper() [2:]}')
elif base == 3:
    print(f'O número {n} na base octal é: {oct(n) [2:]}')
else:
    print('Opção INVÁLIDA. Favor selecionar 1, 2 ou 3. Começe novamente.')
