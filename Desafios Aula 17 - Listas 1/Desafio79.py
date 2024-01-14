"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos t odos os valores únicos digitados, em ordem crescente."""

lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print(f'Vc adicionou {n} em "lista".')
    else:
        print(f'O número {n} já está na lista.')
    resp = str(input('Deseja resp? [S/N] ').upper())
    while resp not in 'SN':
        resp = str(input('Deseja resp? [S/N] ').upper())
    if resp == "N":
        break

print(sorted(lista))
