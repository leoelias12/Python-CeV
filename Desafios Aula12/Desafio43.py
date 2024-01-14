"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input('Digite o seu peso em kg:\n'))
altura = float(input('Digite a sua altura em metros:\n'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Vc está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f}. Vc está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2f}. Vc está em sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é {imc:.2f}. Vc está com obesidade.')
else:
    print(f'Seu IMC é {imc:.2f}. Vc está com obesidade mórbida.')
