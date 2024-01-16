import moeda
from time import sleep

print('=' * 50)
print(f'{"Calculadora de porcentagem, dobro e metade":^50}')
print('=' * 50)
print()
valor = float(input('Digite o valor a ser calculado: R$'))
percent = float(input('Digite a porcentagem a ser adicionada e subtraida: '))
print()
print('=' * 50)
print(f'{"Calculando valores finais...":^50}')
print('=' * 50)
sleep(1)
print()
print(f'O valor R${valor:.2f} aumentado em {percent}% é: R${moeda.aumentar(valor, percent)}')
print(f'O valor R${valor:.2f} aumentado em {percent}% é: R${moeda.diminuir(valor, percent)}')
print(f'O dobro de R${valor:.2f} é: R${moeda.dobro(valor)}')
print(f'A metade de R${valor:.2f} é: R${moeda.metade(valor)}')
