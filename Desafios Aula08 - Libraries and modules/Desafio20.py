"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle

a1 = str(input("nome do aluno 1:"))
a2 = str(input("nome do aluno 2:"))
a3 = str(input("nome do aluno 3:"))
a4 = str(input("nome do aluno 4:"))


list = [a1, a2, a3, a4]
shuffle(list)

print("A ordem será: {}".format(list))
