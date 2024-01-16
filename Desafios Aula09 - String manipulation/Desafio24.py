"""crie um programa que leia o nome de uma cidade e diga se ela começa ou nao
com a palavra 'SANTO'."""

cidade = (input('Digite o nome da cidade: ')).split()

print('Santo' in cidade[0].title())