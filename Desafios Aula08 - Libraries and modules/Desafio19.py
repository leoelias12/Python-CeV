"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome dos alunos e escrevendo na tela o nome do escolhido."""

import random

a1 = str(input("nome do aluno 1:"))
a2 = str(input("nome do aluno 2:"))
a3 = str(input("nome do aluno 3:"))
a4 = str(input("nome do aluno 4:"))
a5 = str(input("nome do aluno 5:"))
a6 = str(input("nome do aluno 6:"))
a7 = str(input("nome do aluno 7:"))
a8 = str(input("nome do aluno 8:"))
a9 = str(input("nome do aluno 9:"))
a10 = str(input("nome do aluno 10:"))
a11 = str(input("nome do aluno 11:"))


list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, 10, a11]

escolhido = random.choice(list)

print("o escolhido é: {}".format(escolhido))
