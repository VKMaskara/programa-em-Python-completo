from datetime import date
from colorama import Fore, Style, init

init(autoreset=True)  # Garante que a cor volte ao normal automaticamente

# Cria o dicionário
pessoa = {}

# Entrada de dados com cores
print(Fore.BLUE + "=== Cadastro de Pessoa ===" + Style.RESET_ALL)
pessoa['Nome'] = input(Fore.GREEN + 'Nome: ' + Style.RESET_ALL)
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
    
