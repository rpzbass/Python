import random

#Encadeamento de laços de repetição
for cont_ex in range(1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5,0,-1):
        print(f'\tvalor : {cont_in}')

print('Fim dos laços')


for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(6):
        num = random.randint(1,100)
        print(f'Valor: {num}')