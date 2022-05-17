# Teste de RPG baseado em Texto usando Pygame

import cmd
import textwrap
import sys
import os
import time
import random

larguraTela = 100


# Configuração do Jogador

class Jogador:
    def __init__(self):
        self.nome = ''
        self.vida = 0
        self.mana = 0
        self.estado = []
        self.localizacao = ''


meuJogador = Jogador()


# Tela de título

def telaDeSelecao():
    opcao = input("> ")
    if opcao.lower() == "play":
        jogar()  # Placeholder
    elif opcao.lower() == "menu":
        menu()
    elif opcao.lower() == "quit":
        sys.exit()
    while opcao.lower() not in ['play', 'menu', 'quit']:
        print("Por favor digite um comando válido.")
        opcao = input("> ")
        if opcao.lower() == "play":
            jogar()  # Placeholder
        elif opcao.lower() == "menu":
            menu()
        elif opcao.lower() == "quit":
            sys.exit()


def tela():
    os.system('clear')
    print('############################')
    print('#  Escape From São Paulo!  #')
    print('############################')
    print('         - Play  -          ')
    print('         - Menu  -          ')
    print('         - Quit  -          ')
    print('   Copyright 2022 AZ0iC.me  ')
    telaDeSelecao()


def menu():
    print('############################')
    print('#  Escape From São Paulo!  #')
    print('############################')
    print('Este jogo funciona com      ')
    print('comandos escritos aprendidos')
    print('durante o jogo, ANOTE tudo! ')
    print('Boa sorte e não morra.      ')
    telaDeSelecao()


def jogar():
    pass


NOMEZONA = ''
EXAMINAR = 'examinar'
DESCRICAO = 'descricao'
SOLUCIONADO = False
ACIMA = 'up', 'acima', 'cima', 'w'
ABAIXO = 'down', 'abaixo', 'baixo', 's'
ESQUERDA = 'left', 'esquerda', 'a'
DIREITA = 'right', 'direita', 'd'

lugaresSolucionados = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                       'b1': False, 'b2': False, 'b3': False, 'b4': False,
                       'c1': False, 'c2': False, 'c3': False, 'c4': False,
                       }

mapa = {
    'a1': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        ACIMA: 'up' or 'acima' or 'cima' 'w',
        ABAIXO: 'down' or 'abaixo' or 'baixo' or 's',
        ESQUERDA: 'left' or 'esquerda' or 'a',
        DIREITA: 'right' or 'direita' or 'd'

    }
}
