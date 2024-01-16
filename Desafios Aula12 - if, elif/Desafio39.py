"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do pessoao do alistamento.
Seu programa também deverá mostrar o pessoao que falta ou que passou do prazo."""
from datetime import date

hoje = date.today().year
sexo = int(input('Qual o seu sexo?\n[1] Masculino\n[2] Feminino\n'))
if sexo == 2:
    print('Como você é mulher, você nao precisa se alistar')
else:
    ano = int(input('Digite o ano em que você nasceu.\n'))
    idade = hoje - ano

    if idade < 18:
        print(f'Você deve se alistar em {18 - idade} anos')
    elif idade == 18:
     print('Você deve se alistar IMEDIATAMENTE!')
    else:
        print(f'Você passou {idade - 18} anos do pessoao de alistamente.')
