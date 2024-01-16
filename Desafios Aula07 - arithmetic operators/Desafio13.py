"13 - Faça um algoritmo que leia o salário de um funcionário, e motre o seu novo salário com 15% de aumento"

salário = float(input("Qual o seu saário atual?"))
novo = salário + (salário*15/100)

print("Seu novo salário com 15% de aumento é: R${:.2f}".format(novo))
