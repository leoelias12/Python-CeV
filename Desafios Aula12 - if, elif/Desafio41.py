"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
from datetime import date

ano = int(input('Para saber sua categoria, insira o seu ano de nascimento:\n'))
idade = date.today().year - ano

if idade <= 9:
    print(f'Com {idade} anos vc se encaixa na categora MIRIM.')
elif 9 < idade <= 14:
    print(f'Com {idade} anos vc se encaixa na categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Com {idade} anosvc se encaixa na categoria JÚNIOR.')
elif 19 < idade <= 25:
    print(f'Com {idade} vc se encaixa na categoria SÊNIOR.')
else:
    print(f'Com {idade} vc se encaixa na categoria MASTER.')
