"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""
s = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
while s not in 'MF':
    s = str(input('Opção inválida. Tente novamente!\nDigite o seu sexo [M/F]')).strip().upper()
print(f'Sexo {s} registrado com sucesso!')
print('Acabou!')
