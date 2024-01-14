from lib import interface


while True:
    resposta = interface.menu(('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'))
    if resposta == 1:
        interface.titulo('pessoas cadastradas')
        try:
            interface.ler()
        except FileNotFoundError:
            print('\033[31mNenhum arquivo criado'
                  '\nCadastre alguém para criar um novo arquivo.\033[m')
    elif resposta == 2:
        interface.titulo('opção 2')
        print(f'"{interface.adiciona()}" adicionado na lista.')
    elif resposta == 3:
        interface.titulo('FINALIZANDO PROGRAMA')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')



