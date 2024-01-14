"8 - escreva um programa que leia um valor em metros e axiba convertido em centimetros e milímetros"

medida = float(input('Digite a quantidade em metros a ser convertida: \n'))
mm = medida*1000
cm = medida*100

print('{:.0f} metros equivalem a {:.0f}mm ou {:.0f}cm'.format(medida, mm, cm))
