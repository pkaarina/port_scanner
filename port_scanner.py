import socket
import json
import time
import threading
from colorama import Fore, Style, init 

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}
____  _  _  ____  ____  _  _  ____  ____  ____  ____ 
 / ___)/ )( \\(  __)(  _ \\( \\/ )(  _ \\(  __)(  _ \\/ ___)
 \\___ \\) \\/ ( ) _)  )   / )  /  ) _ ( ) _)  )   /\\___ \\
 (____/\\____/(____)(__\\_)(__/  (____/(____)(__\\_)(____/
{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}Port Scanner - by Karina Ferreira {Style.RESET_ALL}
"""
    print(banner)

#Dicionário de serviços conhecidos
SERVICES = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3306: 'MySQL',
    3389: 'RDP'
}

#Função para escanear uma porta
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    start_time = time.time()
    result = sock.connect_ex((host, port))
    end_time = time.time()

    response_time = round((end_time - start_time) * 1000, 2) #Tempo em milissegundos
    sock.close()

    return {
        "port": port,
        "status":"open" if result == 0 else "closed",
        "service": SERVICES.get(port, "Unknown"),
        "response_time_ms": response_time
    }

#Função para escanear várias portas usando threads
def scan_host(host, port):
    results = []
    threads = []

    for port in port:
        thread = threading.Thread(target=lambda p=port: results.append(scan_port(host,p)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

#Função para salvar os resultados em um arquivo JSON
def save_results(host, results):
    with open(f"{host}_scan_results.json", "w") as file:
        json.dump(results, file, indent=4)
    print(f"{Fore.LIGHTMAGENTA_EX}Resultados salvos em {host}_scan_results.json{Style.RESET_ALL}")

#Função principal
if __name__ == "__main__":
    print_banner()
    target_host = input(f"{Fore.LIGHTRED_EX}Digite o host ou IP para escanear: {Style.RESET_ALL}")
    target_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]

    print(f"{Fore.CYAN}Iniciando varredura no host {target_host}...{Style.RESET_ALL}")
    start_time = time.time()
    scan_results = scan_host(target_host, target_ports)
    end_time = time.time()

    for result in scan_results:
        status_color = Fore.LIGHTMAGENTA_EX if result['status'] == 'open' else Fore.RED
        print(f"{Fore.LIGHTRED_EX}Port {result['port']} ({result['service']}): {status_color} {result['status']}{Style.RESET_ALL} - Tempo de resposta: {result['response_time_ms']} ms")

    print(f"{Fore.CYAN}Varredura concluída em {round(end_time - start_time, 2)} segundos. {Style.RESET_ALL}")
    save_results(target_host, scan_results)