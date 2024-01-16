"12 - Fala um algorítmo que leia o preço de um produto e mostre o seu preço com 5% de desconto"

p = float(input("Qual o preço do produto?"))
d = p*0.95
dif = p-d

print("O produto com preço de R${:.2f} fica com um preço final de R${:.2f} com 5% de desconto aplicado.".format(p, d))
print("Com uma diferença de R${:.2f} a menos".format(dif))
