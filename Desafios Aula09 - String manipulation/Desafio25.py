"""Crie um programa que leia o nome de uma pessoa e diga se possui 'SILVA' no nome."""

nome = str(input('Digite o nome:\n')).strip()
print('Silva' in nome.title())
