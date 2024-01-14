"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
nome1 = ''
nome2 = ''
nome3 = ''
nome4 = ''
idade1 = 0
idade2 = 0
idade3 = 0
idade4 = 0
sexo1 = ''
sexo2 = ''
sexo3 = ''
sexo4 = ''
maioridade = 0
noman = 0
nowoman = 0
menor20 = 0
hnome = ''
for c in range(1, 5):
    print(f'-----{c}ª pessoa-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if c == 1:
        nome1 = nome
        idade1 = idade
        sexo1 = sexo
    elif c == 2:
        nome2 = nome
        idade2 = idade
        sexo2 = sexo
    elif c == 3:
        nome3 = nome
        idade3 = idade
        sexo3 = sexo
    elif c == 4:
        nome4 = nome
        idade4 = idade
        sexo4 = sexo
    if sexo.upper() == 'M':
        noman = noman + 1
        if idade > maioridade:
            maioridade = idade
            hnome = nome
    elif sexo.upper() == 'F':
        nowoman = nowoman + 1
        if idade < 20:
            menor20 = menor20 + 1

print(f'A média de idade do grupo é {(idade1 + idade2 + idade3 + idade4) / 4}')
if noman == 0:
    print('Não existem homens no grupo')
else:
    print(f'O homem mais velho se chama {hnome} e tem {maioridade} anos.')
if nowoman == 0:
    print('Não existe nenhuma mulher com menos de 20 anos no grupo')
else:
    print(f'O número de mulheres com menos de 20 anos no grupo é: {menor20}')
