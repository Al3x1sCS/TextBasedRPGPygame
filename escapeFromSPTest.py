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
OPCAOA = '1', 'a', 'bom'
OPCAOB = '2', 'b', 'neutro bom'
OPCAOC = '3', 'c', 'neutro mal'
OPCAOD = '4', 'd', 'mal'

historia = {'a1': False, 'b1': False, 'c1': False, 'd1': False,
            'a2': False, 'b2': False, 'c2': False, 'd2': False,
            'a3': False, 'b3': False, 'c3': False, 'd3': False,
            'a': False, 'b': False, 'c': False, 'd': False,
            }

# historiaAntiga = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
#                   'b1': False, 'b2': False, 'b3': False, 'b4': False,
#                   'c1': False, 'c2': False, 'c3': False, 'c4': False,
#                   }

progressao = {
    'a1': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a2',
        OPCAOB: 'b2',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b1': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a2',
        OPCAOB: 'b2',
        OPCAOC: 'c2',
        OPCAOD: ''
    },
    'c1': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b2',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'd1': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'a2': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a3',
        OPCAOB: 'b3',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b2': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a3',
        OPCAOB: 'b3',
        OPCAOC: 'c3',
        OPCAOD: ''
    },
    'c2': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b3',
        OPCAOC: 'c3',
        OPCAOD: 'd3'
    },
    'd2': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'a3': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a',
        OPCAOB: '',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b3': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b',
        OPCAOC: '',
        OPCAOD: ''
    },
    'c3': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c',
        OPCAOD: ''
    },
    'd3': {
        NOMEZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: '',
        OPCAOD: 'd'
    }
}
