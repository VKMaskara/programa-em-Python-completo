from datetime import date
from colorama import Fore, Style, init
import os

init(autoreset=True)  # Garante que a cor volte ao normal automaticamente

while True:
    # Cria o dicionário
    pessoa = {}

    # Entrada de dados com cores
    os.system('cls')
    print(Fore.BLUE + "=== Cadastro de Pessoa ===" + Style.RESET_ALL)
    pessoa['Nome'] = input(Fore.GREEN + 'Nome (ou "sair" para encerrar): ' + Style.RESET_ALL)
    
    if pessoa['Nome'].lower() == 'sair':
        print(Fore.YELLOW + "\nPrograma encerrado!" + Style.RESET_ALL)
        break
        
    ano_nasc = int(input(Fore.GREEN + 'Ano de nascimento: ' + Style.RESET_ALL))
    pessoa['Idade'] = date.today().year - ano_nasc
    pessoa['CPTS'] = int(input(Fore.GREEN + 'Carteira de trabalho (0 se não tiver): ' + Style.RESET_ALL))

    # Se a pessoa tiver carteira de trabalho
    if pessoa['CPTS'] != 0:
        pessoa['Ano_contratacao'] = int(input(Fore.GREEN + 'Ano de contratação: ' + Style.RESET_ALL))
        pessoa['Salario'] = float(input(Fore.GREEN + 'Salário: R$ ' + Style.RESET_ALL))
        pessoa['Idade para se aposentar'] = (pessoa['Ano_contratacao'] + 35) - ano_nasc

    # Mostra o resultado
    print(Fore.MAGENTA + '-=' * 30)
    print(Fore.BLUE + ">>> Resultado do Cadastro <<<")
    for chave, valor in pessoa.items():
        print(Fore.GREEN + f'{chave}: {valor}')
    print(Fore.MAGENTA + '-=' * 30 + Style.RESET_ALL)
    
    input(Fore.YELLOW + "\nPressione ENTER para continuar..." + Style.RESET_ALL)
