#PROGRMA QUE GERENCIA O APROVEITAMENTO DE JOGADORES DE FUTEBOL

import os
import time
import matplotlib.pyplot as plt

# codigo e cores para terminal
verde = '\033[1;32m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
reset = '\033[0m'


def limpar_tela():
    """
    Limpa a tela do terminal.
    windows: cls
    linux/mac: clear
    """
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal de acordo com o sistema operacional

def grafico_aproveitamento():
    # Gerar gráfico de barras do aproveitamento dos jogadores
    # Dados para o gráfico
    graf_jogadores = []
    graf_gols = []
    for jogador in tabela:
        graf_jogadores.append(jogador['nome'])
        graf_gols.append(jogador['total'])
    
    #Criar o gráfico
    plt.bar(graf_jogadores, graf_gols, color='blue')

    # Adicionar título e rótulos
    plt.title('Aproveitamento dos Jogadores')
    plt.xlabel('Jogadores')
    plt.ylabel('Total de Gols')
    

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()

def grafico_jogador():
    # Gerar gráfico de linha do aproveitamento de um jogador específico
    jogador = tabela[int(busca)]
    
    # Eixo X será a contagem das partidas (1, 2, 3, ...)
    eixo_x_partidas = range(1, len(jogador['gols']) + 1) 
    
    plt.plot(eixo_x_partidas, jogador['gols'], marker='o') # <--- MUDANÇA AQUI
    plt.title(f"Aproveitamento de Gols - {jogador['nome']}")
    plt.xlabel("Partidas")
    plt.ylabel("Gols")
    plt.grid()
    plt.show()


def tabela_jogadores():
    limpar_tela()
    time.sleep(1)
    if not tabela:
        print(f"{vermelho}\nNenhum jogador cadastrado.\n{reset}")
        return

    col_cod = 4
    col_nome = 20
    col_gols = 36
    col_total = 6
    sep = "  "
    total_width = col_cod + col_nome + col_gols + col_total + len(sep) * 3

    print(f"{verde}=" * total_width + reset)
    print(f"{verde}TABELA DE APROVEITAMENTO DOS JOGADORES{reset}".center(total_width))
    print(f"{verde}=" * total_width + reset)
    print(f"{'COD':<{col_cod}}{sep}{'JOGADOR':<{col_nome}}{sep}{'GOLS (por partida)':<{col_gols}}{sep}{'TOTAL':>{col_total}}")
    print(f"{verde}-" * total_width + reset)

    total_geral = 0
    for i, jogador in enumerate(tabela):
        gols_str = ", ".join(str(g) for g in jogador["gols"])
        # Trunca gols_str caso seja muito longo para manter a tabela alinhada
        if len(gols_str) > col_gols:
            gols_str = gols_str[: col_gols - 3] + "..."
        print(f"{i:<{col_cod}}{sep}{jogador['nome']:<{col_nome}}{sep}{gols_str:<{col_gols}}{sep}{jogador['total']:>{col_total}}")
        total_geral += jogador["total"]

    print(f"{verde}=" * total_width + reset)
    print(f"{'TOTAL JOGADORES:'}{len(tabela):>12}{sep} {'GOLS TOTAIS:':<12}{total_geral:>{col_total}}")
    print(f"{verde}=" * total_width + reset)

jogador = dict()
tabela= []

limpar_tela()
while True:
    limpar_tela()

    print(f"{verde}CADASTRO DE JOGADORES DE FUTEBOL{reset}")
    # Adiciona a cor ao prompt. O texto digitado será verde.
    while True:
        nome = input(f'Nome do jogador: {verde}').strip().title()
        if nome and len(nome) >= 2:  # Pelo menos 2 caracteres
            break
        print(f'{vermelho}⚠️ Por favor, digite um nome válido (mínimo 2 letras).{reset}')
        
    print(reset, end='') # Reseta a cor para o que vier depois
    jogador['nome'] = nome
    
    (time.sleep(0.5))

    
    while True:
        partidas = input(f'Quantas partidas {jogador["nome"]} jogou? {verde}')
        print(reset, end='') # Reseta a cor
        if partidas.isdigit() and int(partidas) > 0:
            partidas = int(partidas)
            break
        else:
            print(f'{vermelho}⚠️ Por favor, digite um número válido de partidas.{reset}')

    gols = []
    for i in range(partidas):
        # O reset foi removido da concatenação e a string de cor é apenas para o prompt.
        while True:
            gol = input(f'   Quantos gols na partida {i+1}? {verde}')
            print(reset, end='') # Reseta a cor
            if gol.isdigit():
                gols.append(int(gol))
                break
            else:
                print(f'{vermelho}⚠️ Por favor, digite um número válido de gols.{reset}')

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    tabela.append(jogador.copy())

  

    resp = input(f'Quer continuar? {verde}[S/N]{reset} ').strip().upper()
    while resp not in ('S', 'N'):
        resp = input(f'Resposta inválida. Quer continuar? {verde}[S/N]{reset} ').strip().upper()
    if resp == 'N':
        break

# ...
        break

tabela_jogadores()
while True:
    resp_graf = input('Deseja ver o gráfico de aproveitamento dos jogadores? [S/N] ').strip().upper()
    if resp_graf in ('S', 'N'):
        break
    print("Resposta inválida. Tente novamente.")
if resp_graf == 'S':
    print("\nGerando gráfico de aproveitamento...")
    grafico_aproveitamento()

while True:
    busca = input('\nMostrar dados de qual jogador? (999 para parar) ')
    if busca == '999':
        break
    if not busca.isdigit() or int(busca) >= len(tabela) or int(busca) < 0:
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {tabela[int(busca)]["nome"]}:')
        for i, g in enumerate(tabela[int(busca)]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        while True:
            resp_graf_jog = input('Deseja ver o gráfico de aproveitamento deste jogador? [S/N] ').strip().upper()
            if resp_graf_jog in ('S', 'N'):
                break
            print("Resposta inválida. Tente novamente.")

        if resp_graf_jog == 'S':
            grafico_jogador()
