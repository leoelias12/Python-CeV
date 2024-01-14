"10 - crie um programa que leia quanto dinheiro uma pessoa tem"
"na carteira e mostre quantos dolares ela pode comprar. U$1 = 3,27"

real = float(input('Dinheiro em carteira:\n'))
dol = 3.27
poder = real/dol

print('Com R${} você pode comprar U${:.2f}.'.format(real, poder))