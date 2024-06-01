try:
    a = int(input('Numerador: '))
    b = int(input('Denomimnador: '))
    r = a / b
except (ValueError, TypeError):
    print('Problema com os tipos de dados digitados!')
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu nao informar dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é: {r}')
finally:
    print('Volte Sempre!')
