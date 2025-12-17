#Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0 

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):  #: dois pontos é um caracter para delimitação de bloco

    print('Resultado Aprovado!')
    print('Parabens!')

elif(media>=5):

     print("Voce está de recuperação!")

else:

    print('Aluno Reprovado!')

print('Sua media é {}' .format(media))


