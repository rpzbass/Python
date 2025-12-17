import random

numeros = [2,4,44,55,33,22,20,40,6,67,88,54]

numero_sorteado = random.choice(numeros)

numero_aposta = int(input('Faca sua aposta: '))

if (numero_aposta == numero_sorteado):

    print(f'Parabens, voce foi sorteado !!!!')

else:

    print(f'Não foi dessa vez, voce perdeu :( ')

    print(f'O numero sorteado é {numero_sorteado}')


