'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em python. No final,coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

import random  # Permite gerar números aleatórios
from operator import itemgetter  # Importa função para selecionar itens
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Cores personalizadas 
AMARELO = Fore.YELLOW
ROSA = Fore.LIGHTMAGENTA_EX
AZUL = Fore.CYAN
BRANCO = Fore.WHITE
VERDE = Fore.GREEN

# Sorteio dos dados para 4 jogadores
jogo = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6)
}

# Mostra os resultados
print(VERDE + Style.BRIGHT + "Resultados dos jogadores:")
for jogador, valor in jogo.items():
    print(BRANCO + f"{jogador} tirou {valor} no dado.")

# Ordena os jogadores pelo valor do dado
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Mostra o ranking final
print(AMARELO + Style.BRIGHT + "\n=== Ranking Final ===")
for i, (jogador, valor) in enumerate(ranking, start=1):
    # Alterna cores para destacar posições
    cor = AZUL if i == 1 else (ROSA if i == 2 else AMARELO)
    print(cor + f"{i}º lugar: {jogador} com {valor}")

print(Style.RESET_ALL)