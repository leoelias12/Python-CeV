"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
 empréstimo será negado."""

casa = float(input('Digite o \033[31mvalor da casa.\033[m\n'))
salario = float(input('Digite o seu \033[31msalário mensal.\033[m\n'))
anos = int(input('Em quantos \033[31manos\033[m deseja pagar?\n'))
prest = casa//(anos*12)

if prest > (salario * 0.30):
    print('Empréstimo foi \033[31mNEGADO\033[m. Valor da prestação é \033[31mmaior\033[m do que 30% do seu salário.')
else:
    print('Empréstimo \033[4;32;40mAPROVADO\033[m.')
