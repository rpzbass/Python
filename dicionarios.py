# Dicionarios

elemento = {
    'Z' : 3, 
    'nome': 'Litio',
    'Grupo': 'Metais Alcalino',
    'Densidade': 0.534
}

print(f'Elemento : {elemento['nome']}')
print(f'Densidade : {elemento['Densidade']}')
print(f'O dicionario possui {len(elemento['Grupo'])}')
print(f'O dicionario possui {len(elemento)}')


print(f'{elemento['nome']}')
#Atualizar uma entrada

elemento['Grupo'] = 'Alcalinos'

print(elemento)

#Adicionar uma entrada

elemento['Periodo'] = 1

#print(elemento)

#Exclusão de itens em dicionarios 

#del elemento['Periodo']

#print(elemento)

#Excluir todos os elementos do dicionario

#elemento.clear()

#print(elemento)

#Deletar elemento

#del elemento

#print(elemento)   #Ocasionará um erro pois o dicionario deixou de existir

#print(elemento.items())
print('-----------------ITEMS---------------------------')
for indice in elemento.items():
    print(indice)

#print mostra apenas as chaves 

print('-------------------CHAVES-------------------------')
for indice2 in elemento.keys():
    print(indice2)

print(f'-----VALORES-------------------------------')
for indice in elemento.values():
    print(f'{indice}')