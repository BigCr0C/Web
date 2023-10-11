#!/usr/bin/env python3


import requests
import argparse
import urllib3
from colorama import Fore, Style  # Importando módulos do colorama

def print_ascii_art():
    ascii_art = """
  ____  _          _____       ___     
 |  _ \(_)        / ____|     / _ \      
 | |_) |_  __ _  | |     _ __| | | | ___ 
 |  _ <| |/ _` | | |    | '__| | | |/ __|
 | |_) | | (_| | | |____| |  | |_| | (__ 
 |____/|_|\__, |  \_____|_|   \___/ \___|
           __/ |                         
          |___/                                                                                                          
                                                                                  
    """
    print(ascii_art)


Fore.YELLOW
urllib3.disable_warnings()
def check_and_save_status_code(url, output_file):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        status_code = response.status_code
        domain = url.split('//')[1] 
        with open(output_file, 'a') as file:
            file.write(f"{domain}\n")
        print(f"Verificado: {domain} - Status Code: {status_code}")
    except requests.exceptions.RequestException as e:
        pass
def check_status_codes(wordlist_file, output_file):
    with open(wordlist_file, 'r') as file:
        urls = file.read().splitlines()
        for url in urls:
            http_url = f"http://{url}"
            https_url = f"https://{url}"
            print(f"Verificando: {http_url}")
            check_and_save_status_code(http_url, output_file)
            print(f"Verificando: {https_url}")
            check_and_save_status_code(https_url, output_file)

if __name__ == "__main__":
    print_ascii_art()
    parser = argparse.ArgumentParser(description="Verifica o status code de uma lista de domínios com 'http://' e 'https' e salva os status code em um arquivo.")
    parser.add_argument("-u", "--wordlist", help="Arquivo de wordlist contendo os domínios a serem verificados", required=True)
    args = parser.parse_args()

    output_file = "status_codes.txt"
    print("Iniciando verificação de status code...")
    check_status_codes(args.wordlist, output_file)
    print("Verificação de status code concluída. Os resultados foram salvos em", output_file)
