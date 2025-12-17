import smtplib
#Teste de mon para aplicar no pfsense
remetente = ""
destinatario = ""
assunto = "Teste de E-mail"
mensagem = "Teste de envio de email"

# Montando o e-mail no formato PLAIN
conteudo = f"From: {remetente}\nTo: {destinatario}\nSubject: {assunto}\nContent-Type: text/plain; charset=utf-8\n\n{mensagem}"

# Configurar o servidor SMTP (altere conforme necessário)
servidor_smtp = ""

try:
    with smtplib.SMTP(servidor_smtp, 25) as servidor:  # Porta 25 geralmente para conexões abertas
        servidor.sendmail(remetente, destinatario, conteudo)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")