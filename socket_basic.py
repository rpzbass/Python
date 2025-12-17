import socket 

destino = "www.google.com.br"
porta = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client.connect((destino,porta))
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
resposta = client.recv(4096)


print(resposta.decode())


