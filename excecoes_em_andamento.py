# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# Blocos Try ... except


def div(k,j):
    return round(k / j, 2)

if __name__ == "__main__":
    while True:
         try:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite outro numero:'))
            break
         except ValueError:
            print(f'Valor informado e incorreto')
    try:
        r = round(n1 / n2, 2)
    except ZeroDivisionError:
        print(f'Nao e possivel dividir por zero')
    else: 
        print(f'Resultado:  {r}')
    