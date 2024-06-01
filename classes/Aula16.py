#  Tuplas sao imutaveis (impossivel de modificar)
lanche = 'hambuerger', 'suco', 'pizza', 'pudim'

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('-' * 30)

for cont in range(0, len(lanche)):
    print(lanche[cont])

print('-' * 30)

for comida in lanche:
    print(f'eu vou comer {comida}')