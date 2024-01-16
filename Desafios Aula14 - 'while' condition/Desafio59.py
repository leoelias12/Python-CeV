menu = '[1] somatotr\n' \
       '[2] multiplicar\n' \
       '[3] maior número\n' \
       '[4] novos números\n' \
       '[5] sair do programa\n'
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
teste = False

print(f'\n>>>MENU DE AÇÕES<<<')

while not teste:
    escolha = int(input(f'{menu}\n>>>>> Escolha uma ação: '))
    if 1 <= escolha <= 4:
        teste = True
        if escolha == 1:
            print(f'\033[35msomatot: {x} + {y} = {x + y}\033[m')
        elif escolha == 2:
            print(f'\033[35mmultiplicar: {x} * {y} = {x * y}\033[m')
        elif escolha == 3:
            if x == y:
                print('\033[35mnão há número maior. Ambos são iguais\033[m')
            elif x > y:
                print(f'\033[35mo maior número é: {x}\033[m')
            else:
                print(f'\033[35mo maíor número é: {y}\033[m')
        elif escolha == 4:
            x = int(input('Digite o primeiro valor: '))
            y = int(input('Digite o segundo valor: '))
        teste = False
        print('=' * 24, '\n')
        print('>>>Escolha outra ação<<<')
    elif escolha == 5:
        print('\033[35mPrograma finalizado.\033[m')
        teste = True
    elif 1 < escolha > 5:
        print('\033[31mTente novamente:\033[m ')
        teste = False
