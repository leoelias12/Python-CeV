"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Digite sua primeira nota:\n'))
nota2 = float(input('Digite sua segunda nota:\n'))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'REPROVADO com média {media}')
elif 5 <= media < 7:
    print(f'RECUPERAÇÃO com média {media}')
else:
    print(f'APROVADO com média {media}')
