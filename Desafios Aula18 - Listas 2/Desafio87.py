"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
text = 'MATRIX EM PYTHON'
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatot = soma3 = maior = n = 0

print('=' * 30)
print(F'{text:^30}')
print('=' * 30)
print()
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um número para {[l]},{[c]}: '))

print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[1;31m[{matrix[l][c]:^5}]\033[m', end='')
        if matrix[l][c] % 2 == 0:  # Soma de todos os valores pares
            somatot += matrix[l][c]
        if c == 2:  # Soma dos valores da terceira coluna
            soma3 += matrix[l][c]
        if l == 1:  # Maior valor da segunda linha
            if c == 0:
                maior = 0
            else:
                if matrix[1][c] > maior:
                    maior = matrix[l][c]
    print()

print()
print(f'Soma dos pares da matriz: {somatot}')
print(f'Soma da 3ª linha: {soma3}')
print(f'Maior número da segunda linha: {maior}')
print()
print('\033[1;31m[F] [I] [M]!')
