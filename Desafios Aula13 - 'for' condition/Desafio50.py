"""Desenvolva um programa que leia seis números inteiros e mostre a somatot apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""
s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
print('\n', '=-' * 12)
print(f'\nA somatot dos números pares dentre os 6 valores dados é de: \033[31m{s}\n\n\n')