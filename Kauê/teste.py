#PROGRMA QUE GERENCIA O APROVEITAMENTO DE JOGADORES DE FUTEBOL

import os


def limpar_tela():
    """
    Limpa a tela do terminal.
    windows: cls
    linux/mac: clear
    """
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal de acordo com o sistema operacional

def tabela_jogadores():
    limpar_tela()
    if not tabela:
        print("\nNenhum jogador cadastrado.\n")
        return

    col_cod = 4
    col_nome = 20
    col_gols = 36
    col_total = 6
    sep = "  "
    total_width = col_cod + col_nome + col_gols + col_total + len(sep) * 3

    print("=" * total_width)
    print("TABELA DE APROVEITAMENTO DOS JOGADORES".center(total_width))
    print("=" * total_width)
    print(f"{'COD':<{col_cod}}{sep}{'JOGADOR':<{col_nome}}{sep}{'GOLS (por partida)':<{col_gols}}{sep}{'TOTAL':>{col_total}}")
    print("-" * total_width)

    total_geral = 0
    for i, jogador in enumerate(tabela):
        gols_str = ", ".join(str(g) for g in jogador["gols"])
        # Trunca gols_str caso seja muito longo para manter a tabela alinhada
        if len(gols_str) > col_gols:
            gols_str = gols_str[: col_gols - 3] + "..."
        print(f"{i:<{col_cod}}{sep}{jogador['nome']:<{col_nome}}{sep}{gols_str:<{col_gols}}{sep}{jogador['total']:>{col_total}}")
        total_geral += jogador["total"]

    print("=" * total_width)
    print(f"{'TOTAL JOGADORES:':<{col_cod + col_nome + len(sep)}}{len(tabela):>{col_gols}}{sep}{'GOLS TOTAIS:':<12}{total_geral:>{col_total}}")
    print("=" * total_width)


jogador = dict()
tabela= []

limpar_tela()
while True:
    limpar_tela()
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for i in range(partidas):
        gols.append(int(input(f'   Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    tabela.append(jogador.copy())

    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp not in ('S', 'N'):
        resp = input('Resposta inválida. Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

tabela_jogadores()

while True:
    busca = int(input('\nMostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(tabela) or busca < 0:
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {tabela[busca]["nome"]}:')
        for i, g in enumerate(tabela[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')

