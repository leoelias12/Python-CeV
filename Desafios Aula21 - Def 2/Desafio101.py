"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def voto(ano):
    from datetime import date
    permissao = ' '
    if date.today().year - ano < 16:
        permissao = f'Com {date.today().year - ano} anos NÃO VOTA!'
    elif 16 <= date.today().year - ano < 18 or date.today().year - ano >= 65:
        permissao = f'Com {date.today().year - ano} anos, o voto é OPCIONAL'
    else:
        permissao = f'Com {date.today().year - ano} anos, o voto é OBRIGATÓRIO'
    return permissao


#  MAIN
nascimento = int(input('Em que ano vc nasceu? '))
print(voto(int(nascimento)))

