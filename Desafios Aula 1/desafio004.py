n = input('digite algo: ')

print('o tipo primitivo é ', type(n))
print('tem só espaço? ', n.isspace())
print('é numero? ', n.isnumeric())
print('é alfabetico? ', n.isalpha())
print('é alfanumérico? ', n.isalnum())
print('é minúscula? ', n.islower())
print('é maiúscula? ', n.isupper())
print('é capitalizada? ', n.istitle())