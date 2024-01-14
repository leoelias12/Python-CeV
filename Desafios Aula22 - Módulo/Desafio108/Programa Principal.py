import moeda
from time import sleep

print('=' * 50)
print(f'{"Calculadora de porcentagem, dobro e metade":^50}')
print('=' * 50)
print()
currency = str(input('Qual tipo de moeda deseja usar? Ex. R$, U$... '))
valor = float(input(f'Digite o valor a ser calculado: {currency}'))
percent = float(input('Digite a porcentagem a ser adicionada e subtraida: '))
print()
print('=' * 50)
print(f'{"Calculando valores finais...":^50}')
print('=' * 50)
sleep(1)
print()
print(f'O valor {moeda.moeda(valor, currency)} aumentado em {percent}% é: {moeda.moeda(moeda.aumentar(valor, percent), currency)}')
print(f'O valor {moeda.moeda(valor, currency)} aumentado em {percent}% é: {moeda.moeda(moeda.diminuir(valor, percent), currency)}')
print(f'O dobro de {moeda.moeda(valor, currency)} é: {moeda.moeda(moeda.dobro(valor), currency)}')
print(f'A metade de {moeda.moeda(valor, currency)} é: {moeda.moeda(moeda.metade(valor), currency)}')
