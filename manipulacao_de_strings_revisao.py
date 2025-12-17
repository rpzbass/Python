#nome = 'Escola estadual do parana'


#cont = 0
#for palavra in nome.split():
 #   print(f'{cont} {palavra}')
 #   cont += 1


# Exercício: Crie um programa que:
# 1. Pede ao usuário para digitar 5 nomes
# 2. Armazena em uma lista
# 3. Mostra os nomes em ordem alfabética
# 4. Mostra quantos nomes começam com vogal

nomes = []
for i in range(5):
    nome = input('informe o nome: ').strip()
    nomes.append(nome)
cont = 0

novalista = []
for nome in sorted(nomes):
    novalista.append(nome)
    cont += 1

for n in novalista:
    print(n)

vogal = input('Informe a vogal a procurar: ').strip()

for palavra in novalista:
    if vogal in palavra:
        print(f'Vogal encontrada na {palavra}')

        
    
