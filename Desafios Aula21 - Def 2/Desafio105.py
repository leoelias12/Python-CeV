"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""


def notas(qtd, sit=False):
    """
    → Função para analisar as notas e situação de uma turma.
    :param qtd: Quantidades de notas a serem registradas (média do aluno)
    :param sit: Valor opcional para mostrar ou nao a situação da turma
    :return: Dicionário com informações sobre a turma.
    """
    turma = dict()
    nota = list()
    for n in range(1, qtd + 1):
        nota.append(float(input(f'Nota número {n}: ')))
    turma['Total'] = len(nota)
    turma['Maior nota'] = max(nota)
    turma['Menor nota'] = min(nota)
    turma['Média'] = f'{sum(nota) / len(nota):.2f}'
    print(f'=== {qtd} notas foram adicionadas ===')
    resp = str(input('Deseja incluir a situação da turma na análise?[S/N] ')).strip().upper()
    if resp == 'S':
        sit = True
    if sit:
        if (sum(nota) / len(nota)) < 6:
            turma['Situação'] = 'Ruim'
        if 6 < (sum(nota) / len(nota)) < 7:
            turma['Situação'] = 'Razoável'
        elif (sum(nota) / len(nota)) > 7:
            turma['situação'] = 'Boa'
    return turma




#  main
ajuda = str(input('Deseja mostrar ajuda?[S/N] ')).upper().strip()
if ajuda == 'S':
    help(notas)
print('=' * 50)
resposta = notas(int(input('Quantas notas deseja adicionar? ')))
print()
for k, v in resposta.items():
    print(f'{k}: {v}')
print()