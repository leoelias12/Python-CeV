"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma
tabular."""
produtos = ('lápis', 2,
            'borracha', 4,
            'caderno', 10,
            'caneta', 3.5,
            'estojo', 7,
            'mochila', 40.80,
            'régua', 4)
print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(' R$', f'{produtos[c]:>6.2f}')
print('=' * 40)