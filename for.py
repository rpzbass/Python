#Laço for 

#Iterando uma lista
lista = ['Golf','Gol','Marea','Fusca', 'Gol GTI']
num = 0
for item in lista:
    num += 1
    print(f'{num} Carro: {item}')


#Iterando uma string com aplicação de condicional
palavra = 'Ronaldo'
for letra in palavra:
    if(letra == 'l' or letra == 'L'):
       print(f'Encontrada a letra {letra}')
    print(f'{letra}')


nome = input('Informe seu nome: ')

for x in range(100): # Funcao range(valor_inicial, valor_final, incremento)
    print(f'{x+1} {nome}')


print(f'----------------------------------------------')

for y in range(10, 30, 2):  #Vai gerar numeros de 2 em 2 se for decremento usar -2
     print(f'{y}')


pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')

for pedra in pedras:
    if (pedra == 'Safira'):
        continue
    print(pedra)