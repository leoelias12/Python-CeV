"""faça uma tabuada utilizando o FOR"""

n = int(input('De qual número vc deseja saber a tabuada?\n'))
for t in range(1, 11):
    print(f'{n} x {t:2} = {t * n:2}')
