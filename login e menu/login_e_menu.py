import getpass  # ocultar senha ao digitar
import random
import sys  # função de finalizar o código e sair do loop
import os
import time
from datetime import datetime

# --- VARIÁVEIS DE CONFIGURAÇÃO (Credenciais) ---
usuario_correto = "kaique"
senha_correta = "1245"
tentativas_maximas = 3


def fazer_cadastro():
    global usuario_correto, senha_correta
    print("\n--- TELA DE CADASTRO ---")
    novo_usuario = input('Insira o nome de usuario que deseja registrar: ').strip()
    nova_senha = input('Insira a senha: ').strip()  # 1245

    usuario_correto = novo_usuario
    senha_correta = nova_senha

    print("Cadastro realizado com sucesso! Você será levado ao menu principal.")
    return True


def fazer_login():
    tentativas = tentativas_maximas

    while tentativas > 0:
        # 1. Solicita as credenciais
        usuario = input("Usuário : ").strip()
        senha = getpass.getpass("Senha : ").strip()

        # 2. Verifica as credenciais
        if usuario == usuario_correto and senha == senha_correta:
            print("\n====================================")
            print("Login bem-sucedido! Acesso liberado.")
            print("====================================\n")
            return True  # Login OK
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"\nErro: Usuário ou senha incorretos.")
                print(f"Você tem mais {tentativas} tentativa(s).\n")
            else:
                print("\n====================================")
                print("Número máximo de tentativas excedido.")
                print("====================================")
                return False  # Login Falhou


# ---------- FUNÇÕES QUE REPRESENTAM OS 5 PROGRAMAS ----------
def programa_1():
    print("\n--- Programa 1 ---")
    print("Aqui você coloca a lógica do Programa 1")


def programa_2():
    print("\n--- Programa 2 ---")
    print("Aqui você coloca a lógica do Programa 2.")


def programa_3():
    print("\n--- Programa 3 ---")
    print("Aqui você coloca a lógica do Programa 3.")


def programa_4():
    print("\n--- Programa 4 ---")
    print("Aqui você coloca a lógica do Programa 4.")


def programa_5():
    print("\n--- Programa 5 ---")
    print("Aqui você coloca a lógica do Programa 5.")


# ---------- MENU DE PROGRAMAS (após login) ----------
def menu_de_programas():
    """
    Menu mostrado logo após login bem-sucedido.
    Permite acessar 5 programas, fazer logout (voltar ao menu inicial) ou encerrar.
    """
    while True:
        print("\n====================================")
        print("         MENU DE PROGRAMAS          ")
        print("====================================")
        print("Escolha um dos programas abaixo:")
        print("  1 - Programa 1")
        print("  2 - Programa 2")
        print("  3 - Programa 3")
        print("  4 - Programa 4")
        print("  5 - Programa 5")
        print("  L - Logout (voltar para a tela inicial)")
        print("  E - Encerrar Programa")

        escolha = input("Digite sua opção: ").strip().upper()

        if escolha == "1":
            programa_1()
        elif escolha == "2":
            programa_2()
        elif escolha == "3":
            programa_3()
        elif escolha == "4":
            programa_4()
        elif escolha == "5":
            programa_5()
        elif escolha == "L":
            print("\nFazendo logout e voltando para a tela inicial...")
            return  # volta para o menu inicial (tela_inicial_com_menu)
        elif escolha == "E":
            print("\nEncerrando o programa a pedido do usuário.")
            sys.exit()
        else:
            print(f"Opção inválida ('{escolha}'). Por favor, digite 1-5, L ou E.")


# ----------------------------------------------------------------------
# TELA INICIAL COM MENU (login / cadastro / encerrar)
# ----------------------------------------------------------------------
def tela_inicial_com_menu():
    while True:
        print("\n====================================")
        print("      SIMULADOR DE DADOS - MENU     ")
        print("====================================")
        print("Escolha uma das opções abaixo:")
        print("  (L) - Login")
        print("  (C) - Cadastro")
        print("  (E) - Encerrar Programa")

        escolha = input("Digite sua opção: ").strip().upper()

        if escolha == "L":
            if fazer_login():
                # Ao logar com sucesso, vamos direto para o menu de programas.
                menu_de_programas()
                # Quando o usuário der logout (retorno), voltamos a exibir a tela inicial.
        elif escolha == "C":
            fazer_cadastro()
        elif escolha == "E":
            print("\nEncerrando o programa a pedido do usuário.")
            sys.exit()
        else:
            print(f"Opção inválida ('{escolha}'). Por favor, digite L, C ou E.")


# ----------------------------------------------------------------------
# ESTRUTURA PRINCIPAL (Isto faz o código rodar)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    tela_inicial_com_menu()
