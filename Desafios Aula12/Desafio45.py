"""Crie um programa que faça o computador jogar Jokenpô com você."""
import random
from time import sleep

print('=' * 30)
print('Vamos jogar Jokenpô.\nEscolha sua jogada.\n', '=' * 29)
jogador = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
Digite o número correspondente:\n'''))
pc = int(random.randint(1, 3))
print(pc)

if jogador == 1:
    jogadorc = 'PEDRA'
elif jogador == 2:
    jogadorc = 'PAPEL'
elif jogador == 3:
    jogadorc = 'TESOURA'


print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!\n')

if pc == jogador:
    print(f'PC: {jogadorc}!\nVc: {jogadorc}!\nÉ um empate!')
elif pc == 1:
    if jogador == 2:
        print(f'PC: PEDRA!\nVc: {jogadorc}\nVC GANHOU!')
    elif jogador == 3:
        print(f'PC: PEDRA!\nVC: {jogadorc}\nEu ganhei!')
    else:
        print('iSSO NAO EXISTE!! Vamos de novo!')
elif pc == 2:
    if jogador == 3:
        print(f'PC: PAPEL!\nVc: {jogadorc}\nVC GANHOU!')
    elif jogador == 1:
        print(f'PC: PAPEL!\nVC: {jogadorc}\nEu ganhei!')
    else:
        print('iSSO NAO EXISTE!! Vamos de novo!')
else:
    if jogador == 1:
        print(f'PC: TESOURA!\nVc: {jogadorc}\nVC GANHOU!')
    elif jogador == 2:
        print(f'PC: TESOURA!\nVC: {jogadorc}\nEu ganhei!')
    else:
        print('iSSO NAO EXISTE!! Vamos de novo!')
