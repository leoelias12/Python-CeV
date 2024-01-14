"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
 na ordem correta."""
exp = str(input('Digite uma expressão matemática: '))
abre = 0
fecha = 0

for pos, v in enumerate(exp):
    if v == '(':
        abre += 1
    if v == ')':
        fecha += 1

if abre == fecha:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')