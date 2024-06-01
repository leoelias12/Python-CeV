print('\033[7;40mSalve parça.\033[m')


#  Conversão de decimal para binário/hexadecimal/octal
n = int(input('Digite um número\n'))
binn = bin(n)
hexn = hex(n)
octn = oct(n)
print(f'binário {binn}')
print(f'hexadecimal {hexn}')
print(f'octal {octn}')