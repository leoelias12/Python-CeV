"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""
c = 0
while True:
    print('=' * 30)
    n = int(input('Digite o número desejado: '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:<} = {n * c}')
print('\nFIM')
