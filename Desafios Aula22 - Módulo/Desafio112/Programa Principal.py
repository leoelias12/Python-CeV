from utilidades.moeda import resumo
from utilidades.texto import texto1, texto2
from utilidades.dado import leiadinheiro
from time import sleep

texto1("Calculadora de porcentagem, dobro e metade")
valor = float(leiadinheiro('Digite o valor: '))
aumento = float(input('Digite a porcentagem a ser adicionada: '))
reduzir = float(input('Digite a porcentagem a ser descontada: '))
texto1("Calculando valores finais...")
sleep(0.5)
print(resumo(valor, aumento, reduzir))
