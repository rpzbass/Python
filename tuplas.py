#Tuplas são imutaveis, ou seja não pode ser modificada depois de ser criada
#Tuplas são mais rapidas
#Não pode alterar o conteudo da tupla, depois de criada


tupla = (2,4,6,7,9)

#tupla[1] = 10   exemplo pratico de umatabilidade das tuplacas
print(tupla)

halogenios = ('F','Cl','Br','I','At')

print(halogenios)

print(len(halogenios))

t1 = (1,3,4,4,4,5,67,4,32,8,9,0)

print(t1.count(3))

print(66 in t1 )

# Operações não disponiveis em tuplas: .sort() .append(), .reverse(), .pop()

lista = list(t1)  # Pode converter uma tupla para uma lista 

lista[2] = 21
print(lista)

print(type(lista))
print(type(t1))