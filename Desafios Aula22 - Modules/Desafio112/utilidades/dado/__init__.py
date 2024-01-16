def leiadinheiro(msg):
    while True:
        dinheiro = str(input(msg)).strip()
        if dinheiro.replace(',', '').replace('.', '').isnumeric():
            dinheiro = dinheiro.replace(',', '.')
            break
        else:
            print(f'\033[31mERRO: "{dinheiro}" é um valor inválido!\033[m')
    return dinheiro
