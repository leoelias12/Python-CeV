"Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias"
"pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."

km = float(input("Digite quantos kilometros foram rodados com o carro:"))
dias = int(input("Digite o número de dias do aluguel do carro:"))
preço = (km*0.15)+(dias*60)

print("\nO carro foi alugado por {} dias e rodou {}km.".format(dias, km))
print("Portanto o preço total do aluguel é de R${:.2f}.".format(preço))
