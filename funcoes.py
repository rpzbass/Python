

def valida_dominio(email): 
    if '@' not in email:
       return False
    if '.' not in email:
       return False
    if email.count('@') > 1:
       return False
    valid_domains = ['gmail','yahoo','hotmail','zipmail']
    for domain in valid_domains:
      if domain in email:
         return True
    else:
       return False 
      









if __name__ == "__main__":


 #print(valida_dominio("ronaldo@teste.com"))
     
   email = "ronaldo@teste.com"
  # if not domain in email:
   #E   print('Dominio nao esta na lista')
   #else:
   #   print('O Dominio esta na lista')

   print(f'{valida_dominio(email)}')