nome = 'Curso de Python'
instrutor = 'Ronaldo'

letra = nome[2]
print(letra)

print(len(nome))
print(nome)

print(nome + ' com ' + instrutor )

frase = 'Vamos aprender Python hoje !!!'

palavras = frase.split()
print(palavras)
print(palavras[1])
#IMPRIMINDO A LISTA DE PALAVRAS DA VARIAVEL PALAVRAS DEVIDO O SPLIT FEITO ANTERIORMENTE
for palavra in palavras:
    print(palavra)

#AGORA SE FIZERMOS ISSO COM UMA STRING VAMOS IMPRIMIR UMA LISTA DE LETRAS

#SLICE [0:6]  [-3:]

for letra in nome:
    print(f'letra -> {letra}')

#email = input('informe seu email: ')
#arroba = email.find('@')
#print(f'arroba -> {arroba}')
#usuario = email[0:arroba]
#dominio = email[arroba+1:]

#print(usuario)
#print(dominio)
#print(email[16:19])  # o : mostra que vc quer um range   como se fosse 16 até  ai vazio seria até o que existir

print(f'-------------------------')
produtos = 'carbonato de sódio e óxido de zinco'

#print('sódio' in produtos)
#print('magnésio' in produtos)
#print('magnésio' not in produtos)

#item = 'hipoclorito'
#pos = item.find('clor')

#print(f'ocorrencia localizada na posicao {pos}')

#pos = item.find('flu')

#if (pos == -1):
 #   print('Ocorrencia nao encontrada')

 # MAIUSCULO 

# objeto_celeste = 'galaxia espiral M3'
# print(objeto_celeste.upper())

# mac = '18-56-55-AB-fC'

# new_mac = mac.replace('-',':')

# print(new_mac)

frase = '     Omega 3 e bom para a saude     '

print(f'{frase}')

print(f'{frase.lstrip()}')
print(f'{frase.rstrip()}')

print(f'{frase.strip()}')

print('------------------------------------')
item = 'teste'
pos = item.find('te')
print(pos)

fruta = 'abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.rjust(20,'#'))
print(fruta.center(20,"#"))

print(fruta.startswith('aba')) # metodo que verifica se começa com as palavras inseridas metodo de retorno boleano, case sense

print(fruta.endswith('jo')) # verifica se a string termina com a palavra mostrada retorno boleado
#texto = """      para imprimir docstring
"""
Docstring é uma especie de documentação que podemos inserir dentro de um modulo, funçao ou classe 
"""

veiculo = 'carro'

print('--------------------------')
print(f'{veiculo.endswith('carro')}')

item = 'hipoclorito'

pos = item.find('clor')

print(pos)

pos2 = item.find('flu')
print("------------- teste------------------------")
print(f'{pos2}')

mac = 'a6-b5-a4-b3-cf-8a'

mac2 = mac.replace('-',':')

print(f'{mac2}')

#------------------ FRASE LONGA COM ESPAÇO ---------------

frase = '       Omega 3 e bom para a saude!    '

print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip().upper())



fruta = 'Maracuja'

print(fruta.rjust(20))

print(fruta.center(60,"."))

