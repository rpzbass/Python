def contar(num=11,caractere='+'):
    for i in range(1,num):
        print(caractere)

x = 5 
y = 6 
z = 3

def soma_mult(a,b,c,d):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ == '__main__':
    
   # contar(caractere='*')

   print(f'{soma_mult(5,4,0,4)}')

   print(f'{soma_mult(5,4,1,4)}')