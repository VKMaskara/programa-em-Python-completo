import os
import time


cadastro = []  # lista para armazenar os dados dos alunos
print( 19*"==")
print( f"\n✅ Login bem-sucedido! Bem-vindo! 🎉\n")
print( 19*"==")
print( "\ncarregando sistema...")
time.sleep(3)
os.system('cls')
while True:

    nome = input( f"\n\nDigite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = input( f"\nNota {i+1}: ")
        while not (nota.replace('.', '', 1).isdigit() and 0 <= float(nota) <= 10):
            print( "⚠️ Entrada inválida! Digite uma nota entre 0 e 10.")
            nota = input( f"Nota {i+1}: ")
        notas.append(float(nota))
        
    media = sum(notas) / 4  # calcula a média após inserir todas as notas
    cadastro.append((nome, notas, media))
    print(  40*".")
    continuar = input( "Deseja adicionar mais algum aluno? (S/N) ").upper().strip()
    if continuar == 'N':
        break
os.system('cls')
print( "=" * 35)
print( f"📋  Nº   ⮕   NOME   ⮕   MÉDIA")
print( "=" * 35)

for i, (nome, notas, media) in enumerate(cadastro, start=1):
    print(f"{i}  ⮕   {nome}  ⮕   {media:.2f}")

print( "=" * 35)