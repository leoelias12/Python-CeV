frase = 'Curso em Video Python'

print(frase)
print(frase[9])  # exibe o caractere na posição 9
print(frase[9:14])  # fatiamento começando no caractere 9 e excluindo o 14
print(frase[9:21])
print(frase[9:])  # fatiamento de um ponto até o final
print(frase[9:21:2])  # fatiamento de 9 a 21 pulando 2 caracteres
print(frase[::-1])  #  lendo ao contrario
print(frase[:5])  # fatiamento do inicio ao 5
print("----------")

print(len(frase))  # conta a quantidade de caracteres
print(frase.count('o'))  # conta quantidade de 'o'
print(frase.count('o', 3, 14))  # conta a quantidade de 'o' fatiando
print(frase.find('deo'))  # identifica onde inicia o texto desejado
print(frase.replace('Python', 'Android'))  # replace one word for another
print(frase.upper())  # deixa todas as letras em maiusculo
print(frase.lower())  # deixa todas as letras em minusculo
print(frase.capitalize())  # deixa apenas a primeira letra da string maiuscula)
print(frase.title())  # deixa todas as iniciais maiusculas
print('-------------------')
print('-------------------')

frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip())  # remove espaços inuteis no começo e fim da string
print(frase2.rstrip())  # remove espaços inuteis na direita da string
print(frase2.lstrip())  # remove espaços inuteis na esquerda da string
print(frase.split())  # divide as palavras da string em uma lista
frase = frase.split()
nospace = (''.join(frase))  # juntando as palavras da lista com "-"
print(len(nospace)+1)
print(frase.count)