"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
aluno = dict()

aluno['Nome'] = str(input('Nome do Aluno: ').strip())
while True:
    aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
    if 0 <= aluno['Média'] <= 10:
        break
print()
for k, v, in aluno.items():
    print(f'    - {k}: {v}')
print()
if 6 <= aluno['Média'] < 7:
    print(f'{aluno["Nome"]} está de RECUPERAÇÃO!')
elif aluno['Média'] < 6:
    print(f'{aluno["Nome"]} foi REPROVADO!')
else:
    print(f'{aluno["Nome"]} foi APROVADO!')
