"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não resp a
digitar valores."""
n = int(input('Digite um número inteiro: '))
s = n
c = 1
high = n
low = n
menu = '\n\033[34mO que deseja fazer?\n' \
       '[1] Adicionar mais valores\n' \
       '[2] Parar\033[m\n'
escolha = 1
while escolha != 2:
    print(menu)
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        n = int(input('Digite mais um número inteiro: '))
        c = c + 1
        s = s + n
        if n < low:
            low = n
        elif n > high:
            high = n
        avg = s / c
    elif escolha > 2 or escolha < 1:
        print(f'\n\033[31mOpção inválida. Tente novamente.\033[m\n')
print('\n')
if c == 1:
    print(f'Vc digitou apenas {c} número.')
    print(f'O número digitado é {n}')
else:
    print(f'Vc digitou um total de {c} números.')
    print(f'A média entre os números é de {avg:.2f}.')
    print(f'O maior número é {high}, e o menor número é {low}.')
    print('\nFIM')
