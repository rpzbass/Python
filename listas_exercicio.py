

#Crie um script que peça para o usuaário digitar o nome
#de 5 bebidas favoritas dele, armazenando esses valores em 
#uma lista

lista = []

for valor in range(5):
    lista.append(input('informe os nomes das bebidas: '))     

lista_ordenada = sorted(lista)

for index in range(5):
    print(f'ITEM NUMERO {index} -> {lista_ordenada[index]}')


