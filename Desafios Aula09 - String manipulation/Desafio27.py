"""faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o ultimo nome."""

#nome = str(input('Digite o seu nome:\n').split()).strip()
nome = str(input('Digite o seu nome:\n').strip())
#print(nome[0])
#print(nome[2])  # ultimo nome
print(nome.split()[0])
print(nome.split()[-1])
