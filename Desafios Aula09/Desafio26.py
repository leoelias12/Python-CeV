"""faça um programa que leia uma frase e:
- conte quantas letras 'a' tem.
- em que posição ela aparece a primeira vez
- em que posição ela aparece a ultima vez"""

frase = str(input("Digite uma frase.\n")).strip()
tamanho = len(frase)
print('A aletra "a" aparece {} vezes.'.format(frase.lower().count('a')))
print(frase.lower().find('a')+1)
print(frase.lower().rfind('a')+1)  # ultima vez
