"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import date

reg = {'nome': '', 'idade': 0, 'CTPS': 0}
reg['nome'] = str(input('Nome: ').strip())
ano = int(input('Ano de nascimento: '))
reg['idade'] = date.today().year - ano
reg['CTPS'] = int(input('Carteira de trabalho (0 se nao tiver): '))
if reg['CTPS'] != 0:
    reg['contratação'] = int(input('Ano de contratação: '))
    reg['salario'] = float(input('Salário: '))
    reg['aposentadoria'] = reg['contratação'] + 35 - ano
print()
for k, v in reg.items():
    print(f'    -{k}: {v}', end=' ')
    if k == 'idade' or k == 'aposentadoria':
        print('anos', end='')
    print()
print()
print(f'{"== FIM ==":^15}')
