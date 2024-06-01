teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
#  muda os dados da lista 'teste'
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#  mostra dentro do dado 1 da lista 'galera' a informação 0
print(galera[1][0])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera1 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera1.append(dado[:])
    dado.clear()

print(galera1)