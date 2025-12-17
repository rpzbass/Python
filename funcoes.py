
#Funcoes   é um bloco de codigo que executa uma determinada tarefa, eventualmente pode ter parametros ou não.
#Modularização, Reuso de Código, Legebilidade
#

def mensagem():
    print('Boson treinamentos em tecnologia')
    print('Curso Completo de Python...')



def soma(n1,n2):
    print(n1+n2)


def mult(n1,n2):
    return  n1 * n2



def divisao(a,b):
    if b != 0:
     return a / b
    else:
     return 'Impossivel divisao por zero'


def quadrados(val):
    quadrados = []
    for x in val:
       quadrados.append(x ** 2)
    return quadrados
    
       


if __name__ == '__main__':
    
   # n1 = int(input('Digite um numero: '))
  #  n2 = int(input('Digite outro numero: '))

   # result = divisao(n1,n2)
   # print(f'a divisao de {n1} e {n2} e igual a {result:.1f}')

    valores = [1,2,3,4,5,6,7]
    resultados = quadrados(valores)
    print(f'{resultados}')
