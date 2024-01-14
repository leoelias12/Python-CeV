import moeda
from func_texto import texto1
from time import sleep

texto1("Calculadora de porcentagem, dobro e metade")
#  currency = str(input('Qual tipo de moeda deseja usar? Ex. "R$, U$..." '))
valor = float(input(f'Digite o valor a ser calculado: R$'))
aumento = float(input('Digite a porcentagem a ser adicionada: '))
reduzir = float(input('Digite a porcentagem a ser descontada: '))
print()
texto1("Calculando valores finais...")
sleep(0.5)
print()
print(moeda.resumo(valor, aumento, reduzir))
