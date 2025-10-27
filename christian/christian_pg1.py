import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

cadastro = []  # lista para armazenar os dados dos alunos
print( Fore.YELLOW + "\niniciando sistema...")
time.sleep(3)
os.system('cls')
while True:

    nome = input(Fore.LIGHTBLACK_EX+ f"\n\nDigite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = input(Fore.YELLOW + f"\nNota do {i+1}º Bimestre : ")
        while not (nota.replace('.', '', 1).isdigit() and 0 <= float(nota) <= 10):
            print(Fore.YELLOW + "⚠️ Entrada inválida! Digite uma nota entre 0 e 10.")
            nota = input(Fore.YELLOW + f"Nota {i+1}: ")
        notas.append(float(nota))
        
    media = sum(notas) / 4  # calcula a média após inserir todas as notas

    if media >= 7:
        situacao = Fore.GREEN + "Aprovado ✅"

    elif media < 5:
        situacao  = Fore.RED + "Reprovado ❌"
    elif media >= 5 and media < 7:
        situacao  = Fore.YELLOW + "Recuperação ⚠️ "

    cadastro.append((nome, notas, media, situacao))
    print(  40*".")
    continuar = input( Fore.LIGHTBLACK_EX + "Deseja adicionar mais algum aluno? (S/N) ").upper().strip()
    if continuar == 'N':
        break
os.system('cls')
print( Fore.LIGHTBLACK_EX + "=" * 35)
print( Fore.YELLOW + "📋  Nº   ⮕   NOME   ⮕   MÉDIA  ⮕   SITUAÇÃO")
print( Fore.YELLOW + "=" * 35)

for i, (nome, notas, media, situacao) in enumerate(cadastro, start=1):
    print(f"{i}  ⮕   {nome.upper()}  ⮕   {media:.2f}  ⮕   {situacao}")

print( Fore.LIGHTBLACK_EX + "=" * 35)

while True:

    opc = input(Fore.LIGHTBLACK_EX + '\n🔎 Digite o número do aluno para ver as notas ou "N" para sair: ').strip().upper()
    if opc == 'N':
        os.system('cls')
        print( Fore.LIGHTBLACK_EX + "  Tchau ... Até a próxima! 👋")
        time.sleep(2)
        os.system('cls')
        break

    if opc.isdigit():
        escolha = int(opc) - 1
        if 0 <= escolha < len(cadastro):
            nome, notas, media, situacao = cadastro[escolha]
           

            print( Fore.YELLOW+ "\n\n👤 O aluno escolhido foi:")
            print(  Fore.LIGHTBLACK_EX + f"\n\nAluno: {nome.upper()} | Média: {media:.2f} | Notas do 1º, 2º, 3º e 4º Bimestre : {', '.join(f'{n:.2f}' for n in notas)} | {situacao} 📊\n")
            print(30*"__")
        else:
            print( Fore.RED + "❌ Número inválido. Tente novamente.")
    else:
        print( Fore.RED + '❗ Entrada inválida. Digite apenas o número do aluno ou "N" para sair.')
