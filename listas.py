# LISTA: Representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

#slice  sequencia[inicio:fim:passo]

# valores = notas + notas2      concatenação de lista

notas = [5,7,8,6,9]

print(notas) # lista pura

print(notas[0]) # indice 0

print(notas[0:4]) # range de numeros nesse range de indexação

print(notas[-2:]) # penultimo

print(len(notas)) # tamaho da lista

print(sorted(notas))

print(sorted(notas, reverse=True))

print(sum(notas)) # resultado da soma

print(min(notas))  # resultado minimo dos valores

print(max(notas)) # Resultado maximo dos valores

notas.append(2)

print(notas)
notas.pop() # Remove o ultimo item da lista
print(notas)
notas.pop(3) # Remove da posição 3

notas.insert(3,22)  # Insere o valor na posição 3
