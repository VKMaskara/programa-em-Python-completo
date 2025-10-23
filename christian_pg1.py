import os
import time


cadastro = []  # lista para armazenar os dados dos alunos
print( "\niniciando sistema...")
time.sleep(3)
os.system('cls')
while True:

    nome = input( f"\n\nDigite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = input( f"\nNota do {i+1}º Bimestre : ")
        while not (nota.replace('.', '', 1).isdigit() and 0 <= float(nota) <= 10):
            print( "⚠️ Entrada inválida! Digite uma nota entre 0 e 10.")
            nota = input( f"Nota {i+1}: ")
        notas.append(float(nota))
        
    media = sum(notas) / 4  # calcula a média após inserir todas as notas

    if media >= 7:
        situacao = "Aprovado ✅"
    elif 5 <= media < 7:
        situacao = "Recuperação ⚠️"                     #onde vai falar a situação do aluno
    else:
        situacao = "Reprovado ❌"

    cadastro.append((nome, notas, media))
    print(  40*".")
    continuar = input( "Deseja adicionar mais algum aluno? (S/N) ").upper().strip()
    if continuar == 'N':
        break
os.system('cls')
print( "=" * 35)
print( f"📋  Nº   ⮕   NOME   ⮕   MÉDIA  ⮕   SITUAÇÃO")
print( "=" * 35)

for i, (nome, notas, media) in enumerate(cadastro, start=1):
    print(f"{i}  ⮕   {nome}  ⮕   {media:.2f}  ⮕   {situacao}")

print( "=" * 35)

while True: 
   
    opc = input('\n🔎 Digite o número do aluno para ver as notas ou "N" para sair: ').strip().upper()
    if opc == 'N':
        os.system('cls')
        print( "  Tchau ... Até a próxima! 👋")
        time.sleep(2)
        os.system('cls')
        break

    if opc.isdigit():
        escolha = int(opc) - 1
        if 0 <= escolha < len(cadastro):
            nome, notas, media = cadastro[escolha]
           

            print( "\n👤 O aluno escolhido foi:")
            print( f"\n\nAluno: {nome} | Média: {media:.2f} | Notas do 1º, 2º, 3º e 4º Bimestre : {', '.join(f'{n:.2f}' for n in notas)} | {situacao} 📊\n")
            print(30*"__")
        else:
            print( "❌ Número inválido. Tente novamente.")
    else:
        print( '❗ Entrada inválida. Digite apenas o número do aluno ou "N" para sair.')
