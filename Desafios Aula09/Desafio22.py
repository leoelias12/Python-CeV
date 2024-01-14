"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- nome com tds as letras maiusculas
- nome com tds as letras minusculas
- qtas letras sem espaços
- qtas letras no primeiro nome"""

fullname = str(input('Digite seu nome completo:\n')).strip()

print(fullname.upper())  # nome com tds as letras maiusculas
print(fullname.lower())  # nome com tds as letras minusculas
# -------
print(len(''.join(fullname.split())), 'letras sem espaço')
# ou \/
print(len(fullname) - fullname.count(' '))
# --------
splited = (fullname.split())
print(len(splited[0]), 'letras no primeiro nome')
