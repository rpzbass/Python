
def calcula_elementos(lista):
    listaII = []
    for l in range(1,len(lista)):
        print(f'{l}')
       # listaII[l] = lista[l]*2
        listaII.append(lista[l]*2) 
    return listaII  







if __name__ == "__main__":

    
    list = [1,2,3,4,4,5,6,4,3,3]


    print(calcula_elementos(list))




















