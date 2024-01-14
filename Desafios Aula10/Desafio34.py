"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
 superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""
s = float(input('Digite o salário do funcionário\n'))

if s > 1250:
    print('O salário de R${:.2f} passou a ser R${:.2f}. Um aumento de 10%'.format(s, s * 1.1))
else:
    print('O salário de R${:.2f} passou a ser R${:.2f}. Um aumento de 15%'.format(s, s * 1.15))
