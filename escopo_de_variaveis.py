# Escopo Global e Local 

var_global = "Curso Completo de Python"

def escreve_texto():
    global var_global
    var_global = "Bancos de Dados com SQL"  
    var_local = "Ronaldo Pereira"
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local :{var_local}')


if __name__ == '__main__':
    print(f'Executar a funcao escreve texto()')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente')
    
    print(f'Variavel Gloval:{var_global}')

    #print(f'Variavel Local:{var_local}')

    print(f"{__name__}")