

num = 1

while(num <= 10):

    print(num)

    num += 1

print('Laco encerrado!')


nome = None

while (True):
    print('\nDigite seu nome, ou x para parar')
    
    nome = input()
    
    if(nome == 'x' or nome == 'X'):
    
        break # O break finaliza imediatamente o laço em que está inserido
    
    print(f'Bem vindo, {nome}\n')

    
     
    