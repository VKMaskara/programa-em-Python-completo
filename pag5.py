# Programa de Cadastro de Pessoas
# Usando dicionário + lista

pessoas = []
soma_idades = 0

print("\033[33m" + "="*50)
print("        SISTEMA DE CADASTRO DE PESSOAS")
print("="*50 + "\033[m")

while True:
    pessoa = {}
    pessoa["nome"] = input("Nome: ").strip()
    pessoa["sexo"] = input("Sexo [M/F]: ").strip().upper()
    pessoa["idade"] = int(input("Idade: "))
    
    pessoas.append(pessoa)
    soma_idades += pessoa["idade"]
    
    continuar = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print("\n\033[33m" + "="*50 + "\033[m")
print("\033[33mA) Quantidade de pessoas cadastradas:\033[m", len(pessoas))

media = soma_idades / len(pessoas)
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
print("\033[33mCRÉDITOS:\033[m")
print("\033[33mCristian : página 1 e encerramento\033[m")
print("\033[33mDennys : página 5\033[m")
print("\033[33mJuliana : página 3\033[m")
print("\033[33mMikaelly : página 2\033[m")
print("\033[33mKaique : login e menu\033[m")
print("\033[33mVitor : página 4\033[m")
print("\033[33m" + "="*50 + "\033[m")
print("\033[33mFIM DO PROGRAMA\033[m")
