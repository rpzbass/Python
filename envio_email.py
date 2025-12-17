import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server ='' 
smtp_port = 25
email_user = ''
email_pass = ''


destino = ''
subject = 'Teste'
body = 'Teste de envio de email'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = destino
msg['Subject'] = subject

msg.attach(MIMEText(body, 'Plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
   # server.starttls()
    server.login(email_user, email_pass)
    server.sendmail(email_user, destino, msg.as_string())
    print("EMAIL ENVIADO COM SUCESSO !!!")

except Exception as e:

    print(f"Erro ao enviar o email {e}")

finally:
    server.quit()
