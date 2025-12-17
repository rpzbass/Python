import socket,sys


def testar_tcp(host,porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = sock.connect_ex((host, porta))
    sock.close()
    if resultado == 0:
        print(f"[+] Porta {porta} ABERTA EM {host}")
    else:
        print(f"[-] Porta {porta} FECHADA EM {host}")
        
  
def testar_udp(host,porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    try: 
        sock.sendto(b'teste', (host, porta))
        data, _ = sock.recvfrom(1024)
        print(f"[+] Porta UDP {porta} ABERTA EM {host} (Respondeu: {data})")
    except socket.timeout:
    
        print(f"[-] PORTA UDP {porta} FECHADA EM {host} (TEMPOEXCEDIDO)")
    
    except ConnectionRefusedError:
        print(f"[-] Porta UDP {porta} FECHADA EM {host} (CONEXAO RECUSADA)")

    except ConnectionResetError: 
        print(f"[-] Porta UDP {porta} POSSIVELMENTE FECHADA EM {host} (CONEXAO ENCERRADA PELO SERVIDOR REMOTO)")
    finally:
        sock.close()

def banner():
    print("---------------------------------------------------------------------")
    print(" ____   _____   ______ _______      _______ _______ _______ _______  ")
    print("|_____] |     | |_____/    |            |    |______ |______    |    ")
    print("|       |_____| |    \\_    |            |    |______ ______|    |    ")
    print("---------------------------- by RP v0.1------------------------------")
 
def menu():
    
    print("[1] + TESTE PORTA TCP ")
    print("[2] + TESTE PORTA UDP ")
    print("[3] + SAIR ")

    opcao = input("Informe qual opcao: ")
    match opcao:
        case "1":
            testar_tcp(sys.argv[1],int(sys.argv[2]))
        case "2":
            testar_udp(sys.argv[1],int(sys.argv[2]))
        case "3":
            print("Saindo do Programa")
            sys.exit(0)
            


if __name__ == "__main__":

 if len(sys.argv) != 3:
     banner()
     print("MODO DE USO : PYTHON PORT_TEST.py <IP> <PORTA> ")
     sys.exit(0)


banner()
menu()