import socket

ip = input('Informe o ip: ')
porta = int(input('Informe a porta: '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if s.connect_ex((ip,porta)) == 0:
    print(f'Porta {porta} está aberta !!')

else:
    print(f'Porta {porta} está fechada!!')


