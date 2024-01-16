"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

dis = float(input('Digite a distancia da viagem.'))

if dis <= 200:
    print('Distancia dentro de 200km. O valor da passagem é de R${:.2f}.'.format(dis * 0.50))
else:
    print('Distancia maior do que 200km. O valor da passagem é de R${:.2f}.'.format(dis * 0.45))
