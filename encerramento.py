from datetime import datetime
import os
import time
from colorama import Fore, init

init(autoreset=True)

os.system('cls')
print(Fore.YELLOW + "\n" + "="*80)
print(Fore.YELLOW + "          Obrigado por usar nosso código, eperamos que tenha gostado!          ")
print( Fore.LIGHTBLACK_EX + "\n                          Data: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print(Fore.YELLOW + "="*80)



print(Fore.LIGHTBLACK_EX + "\n                               Colaboradores :               \n")



nomes = {Fore.YELLOW + 'Kaique': 'Login e menu', Fore.LIGHTBLACK_EX + 'Christian': 'Boletim escolar e encerramento', Fore.YELLOW + "Mikaelly": "Jogo do dado", Fore.LIGHTBLACK_EX+ "Juliana": "Aposentadoria", Fore.YELLOW + "Vitor": "Jogador de futebol", Fore.LIGHTBLACK_EX+ "Dennys": "Cadastro de pessoas"}

for nome, tarefa in nomes.items():
    time.sleep(1)
    print(f"{Fore.LIGHTBLACK_EX}• {nome}: {tarefa}")

print(Fore.LIGHTBLACK_EX + "\n\nAté a próxima! ")

print("\n")



