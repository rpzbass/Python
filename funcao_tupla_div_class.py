

#Lembrando que tuplas são imutaveis 


def saudacao(nome):
    print(f'Ola, {nome}! Bem vindo(a)!')


def divisao_zero(a,b):

    if a != 0:
        return a / b
    else:
        return 'Divisao por zero impossivel !'


def cal_simples(n1,n2):
    soma = n1 + n2
    sub = n1 - n2 
    mult = n1 * n2 
    divi = divisao_zero(n1,n2)
    t = (soma,sub,mult,divi)
    return t

           
def classifica_numero(numero):
 try:
     numero = int(numero)
 except ValueError:
     return "Nao e um numero valido"        
 if numero > 0:
   print(f'{numero} Numero positivo')
 elif numero < 0:
   print(f'{numero} Numero negativo')
 elif numero == 0:
   print(f'{numero} Numero igual a zero')    
    



if __name__ == "__main__":


  # saudacao('Fulano')
   
  # print(cal_simples(0,2))
  numero = input("Informe numero")
  print(classifica_numero(numero))


  

