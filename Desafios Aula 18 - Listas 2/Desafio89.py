"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente."""
aluno = list()
lista = list()

while True:
    aluno.append(str(input('Nome: ').strip()))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    lista.append(aluno[:])
    aluno.clear()
    print()
    resposta = str(input('Deseja continuar?[S/N] ').strip())
    print()
    if resposta in 'Nn':
        break

print(f"{'|=========BOLETIM GERAL=========|':^31}")
print(f"\033[1m{'Nª':<4}{'Aluno':<20}\033[m \033[1m{'Média':<11}\033[m")
print('-' * 31)
for i, a in enumerate(lista):
    print(f'{i + 1:<4}{a[0]:<20}{(a[1] + a[2]) / 2: ^8.2f}')

while True:
    print()
    print('=' * 45)
    resposta = str(input('Deseja ver a algum aluno individualmente?[S/N] '))
    if resposta in 'Nn':
        break
    else:
        a = int(input('Digite o número do aluno desejado: '))
        print()
        print('=' * 40)
        print(f"{'Aluno':<20}{'Nota 1':<9}{'Nota 2':<9}{'Média':<9}")
        print(f"{lista[a - 1][0]:<20}", f"{lista[a - 1][1]:<9}", f"{lista[a - 1][2]:<9}")

print()
print('=' * 30)
print(f"{'Programa Finalizado':^30}")
print('=' * 30)
