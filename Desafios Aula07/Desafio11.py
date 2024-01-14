"11 - Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de"
"tinta necessaria pra pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²"

lar = float(input("Qual a Largura da parede?"))
alt = float(input("Qual a altura da parede?"))
area = lar*alt
tinta = area/2

print("A área da parede é de {:.2f}m²".format(area))
print("Para uma parede de {:.2f}m² você precisará de {:.2f}L de tinta".format(area, tinta))
