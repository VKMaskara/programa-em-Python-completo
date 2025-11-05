'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
Inclui loop central onde o usuário pode sair.'''

import random
from operator import itemgetter
from colorama import Fore, Style, init
import os

init(autoreset=True)

AMARELO = Fore.YELLOW
ROSA = Fore.LIGHTMAGENTA_EX
AZUL = Fore.CYAN
BRANCO = Fore.WHITE
def limpar_tela():
    """Limpa a tela no Windows e Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

VERDE = Fore.GREEN

# Limpa a tela antes de executar o programa
limpar_tela()

def jogar():
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

    # Ordena os jogadores pelo valor do dado (do maior para o menor)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

    # Mostra o ranking final
    print(AMARELO + Style.BRIGHT + "\n=== Ranking Final ===")
    for i, (jogador, valor) in enumerate(ranking, start=1):
        cor = AZUL if i == 1 else (ROSA if i == 2 else AMARELO)
        print(cor + f"{i}º lugar: {jogador} com {valor}")
    print(Style.RESET_ALL)

def main():
    try:
        while True:
            resposta = input("Pressione ENTER para jogar ou digite 's' para sair: ").strip().lower()
            if resposta == 's':
                print("Encerrando o jogo. Até mais!")
                break
            jogar()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Saindo.")

if __name__ == "__main__":
    main()