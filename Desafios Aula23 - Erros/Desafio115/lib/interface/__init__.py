def titulo(msg):
    print('-' * 45)
    print(msg.center(45).upper())
    print('-' * 45)


def menu(lista):
    titulo('Menu principal')
    for i, o in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{o}\033[m')
    print('-' * 45)
    opc = validaEscolha()
    return opc



def validaEscolha():
    while True:
        try:
            resp = int(input('\033[32mSua escolha: \033[m'))
        except(TypeError, ValueError):
            print('\033[31mERRO: Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não escolher uma opção!\033[m')
            print(f'{titulo("finalizando sistema")}\033[m')
            return 0
        else:
            return resp


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[30;41m ERRO! Digite um número INTEIRO! \033[m')
        else:
            break
    return num


def adiciona():
    f = open('pessoas.txt', 'a+')
    nome = str(input('Nome: ').title())
    idade = leiaint('Idade: ')
    f.write(f'{nome};{idade}\n')
    return nome, idade


def ler():
    f = open('pessoas.txt', 'r')
    for linha in f:
        content = linha.split(';')
        content[1] = content[1].replace('\n', '')
        print(f'{content[0]:<37}{content[1]:>3} anos')
    f.close()
