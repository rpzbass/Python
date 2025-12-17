
def mensagem(m):
    print(f"{m}")


def lista(lista):
    for item in lista:
        print(f'{item}')


def lista2(lista):
    for n in range(len(lista)):
      lista[n] +=  ' ' + str(n)  
    for item in lista:
        print(f'{item}')


def lista2_otimizado(lista):
    for n in range(len(lista)):
        print(f'{lista[n]}  {str(n)}')


def valida_domain_email(email):
    domain_validos = ['gmail','hotmail','yahoo']
    for domain in domain_validos:
        if domain in email:
            return True
        else:
            return False



def validar_email(email):
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    if email.count('@') > 1:
        return False
    if not valida_domain_email(email):
        return False
    return True



if __name__ == '__main__':

#    mensagem('Ola tudo bem')
#    nomes = ['Gol','Joao','Jeca','Jorge','Luiz']
    
    #lista2(nomes)

#    lista2_otimizado(nomes)
      
    email = input('Informe o email: ').strip() 
    
    if (validar_email(email)):
       
        print(f'Email {email} validado !!! :) ')
    else:
        print(f'Email {email} invalido :(')

  #  print(f'{valida_domain_email('ronaldo@google.com')}')