"Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."

c = float(input("Digite a temperatura em Celcius:"))
f = (c*(9/5)+32)

print("{:.1f}ºC equivale a {:.1f}ºF".format(c, f))