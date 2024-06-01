num = [2, 5, 9, 1]
num[2] = 3 #  muda o elemento 2 para o número 3
num.append(7) #  adiciona mais um elemento
num.sort(reverse = True) #  sort na lista (reverse)
num.insert(2, 0) #  insere o 0 na posição 2
num.pop() #  Remove o ultimo elemento se nao for expecificado
if 5 in num:
    num.remove(5)
else:
    print('Nao encontrei o número 5.')
print(num)
print(f'Essa lista tem {len(num)} elementos.\n')
print('=' * 30)

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei no final da lista\n')
print('=' * 30)

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'\nLista A: {a}')
print(f'Lista B: {b}')
