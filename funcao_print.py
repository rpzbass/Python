#Funcao print


# Sintaxe:
# print(objetos, argumentos)  ex: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

mensagem = 'Funçao print()'

print(mensagem)

nome = 'Ronaldo'

canal = 'Narnia city'

print(nome ,' - ',canal)


nome2 = input('digite seu nome: ')
msg = 'Olá ' + nome + '! Bem-vindo ao curso de Python! ' # Por padrão 

print(msg)
print('Outro Texto')

carro = 'golf'
cor = 'vemelho'
ano = 2015

print('Nome do carro é {0} , a cor é {1}  e o ano é {2}'.format(carro,cor,ano))

print(f'Nome do carro é {carro} , a cor é {cor}  e o ano é {ano}')

# Formatação de valores flutuantes 

valor = 125.578587875
print(f'O valor e {valor:.2f}')

print(f'O valor formatado e {valor:.1f}')

# Caracteres de escape 

print(f'Carro:\t{carro}\tCor:\t{cor}\tano:\t{ano}')