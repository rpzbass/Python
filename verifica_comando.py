
def verificar_comando(comando):
    
    caracteres_suspeitos = [';','&','|','$']

    for caractere_suspeito in caracteres_suspeitos:

        if caractere_suspeito in comando:
            return 'Comando Suspeito'
            break
    else:
        return 'Comando Seguro'
        


comando_usuario = input()

print(verificar_comando(comando_usuario))