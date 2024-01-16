"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros"""

print('{:=^30}'.format(' Lélias Store '))
normal = float(input('Digite o preço original do produto:\n'))
print('escolha a forma de pagamento\n'
      '[1] Dinheiro (10% de desconto)\n[2] Cartão de Débito (5% de desconto)\n[3] Até 2x no cartão\n'
      '[4] A partir de 3x no cartão (20% de juros)\n')
pagamento = int(input('Digite sua escolha:\n'))

if pagamento == 1:
    print('Forma de pagamento escolhida: \033[31mDINHEIRO\033[m.')
    print(f'Com 10% de desconto, vc pagará apenas R${normal * 0.9:.2f}')
elif pagamento == 2:
    print('Forma de pagamento escolhida: \033[31mA vista no cartão\033[m.')
    print(f'Com 5% de desconto, vc pagará apenas R${normal * 0.95:.2f}')
elif pagamento == 3:
    print('Forma de pagamento escolhida: \033[31mAté 2x no cartão\033[m.')
    print(f'Vc pagará o preco original de R${normal}')
elif pagamento == 4:
    print('Forma de pagamento escolhida: \033[31mA partir de 3x no cartão\033[m.')
    parcelas = int(input('Quantas parcelas?\n'))
    print(f'Vc pagará um juros de 20%: O valor ficará R${normal * 1.2} dividido em {parcelas} parcelas'
          f' de R${normal / parcelas}')
else:
    print('\033[31mOpção inválida\033[m. Tente novamente.')
