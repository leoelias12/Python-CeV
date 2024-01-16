"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = int(input('Qual a velocidade em que o carro estava?\n'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Vc estava {}km/h acima da velocidade! A sua multa é de R${:.2f}! SE FUDEU!'.format(velocidade-80, multa))
else:
    print('Vc estava dentro do limite de velocidade.')

if velocidade <= 20:
    print('Acelera essa merda seu bundão!')