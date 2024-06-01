nome = str(input('Digite o seu nome.\n'))

if nome == 'Leonardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Eduardo' or nome == 'Marcelo':
    print('Seu nome é bem comum no brasil.')
elif nome in 'Ana Maria Marina Beatriz':
    print('Seu nome é feminino')
else:
    print('Seu nome é normal')
print(f'Tenha um bom dia \033[31m{nome}')
