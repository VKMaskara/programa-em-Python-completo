import os
import sys

# Programa de Cadastro de Pessoas
# Usando dicionário + lista

pessoas = []
soma_idades = 0

 # Limpa a tel
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[33m" + "="*50)
print("        SISTEMA DE CADASTRO DE PESSOAS")
print("="*50 + "\033[m")
while True:
    pessoa = {}
    pessoa["nome"] = input("Nome: ").strip()
    # valida sexo
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
       

        if sexo in ('M', 'F'):
            pessoa["sexo"] = sexo
            break
        print("Entrada inválida. Digite M ou F.")
    # valida idade
    while True:
        try:
            idade = int(input("Idade: ").strip())
            if idade < 0:
                print("Idade inválida. Informe um número não-negativo.")
                continue
            pessoa["idade"] = idade
            break
        except ValueError:
            print("Idade inválida. Informe um número inteiro.")

    pessoas.append(pessoa)
    soma_idades += pessoa["idade"]

    continuar = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print("\n\033[33m" + "="*50 + "\033[m")
print("\033[33mA) Quantidade de pessoas cadastradas:\033[m", len(pessoas))

if len(pessoas) > 0:
    media = soma_idades / len(pessoas)
else:
    media = 0.0

print("\n\033[33m" + "="*50 + "\033[m")
print(f"\033[33mB) A média de idade das pessoas é:\033[m {media:.2f}")

print("\n\033[33m" + "="*50 + "\033[m")
print("\033[33mC) Lista de mulheres cadastradas:\033[m")
for p in pessoas:
    if p["sexo"] == "F":
        print(f" - {p['nome']}")

print("\n\033[33m" + "="*50 + "\033[m")
print("\033[33mD) Pessoas com idade acima da média:\033[m")
for p in pessoas:
    if p["idade"] > media:
        print(f" - {p['nome']} ({p['idade']} anos)")

print("\n\033[33m" + "="*50 + "\033[m")
print("        FIM DO PROGRAMA DE CADASTRO")

# Opção para fechar o programa ou retornar ao menu
while True:
    fechar = input("\nDeseja fechar o programa? [S/N]: ").strip().upper()
    if fechar in ('S', 'N'):
        break
    print("Entrada inválida. Digite S para sim ou N para não.")

# Se for 'N', o fluxo segue para o MENU DE PROGRAMAS abaixo
# ----------------------------------------------------------------------
# MENU DE PROGRAMAS