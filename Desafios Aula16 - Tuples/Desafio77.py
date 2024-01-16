"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras = ('ESTUDAR', 'APRENDER', 'CURSO', 'PYTHON', 'PROGRAMAR', 'CODIGO', 'FUTURO', 'TRABALHAR', 'ARARA', 'abacate', 'xerife')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
