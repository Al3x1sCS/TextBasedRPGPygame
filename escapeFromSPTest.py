# Teste de RPG baseado em Texto usando Pygame
#

import cmd
import textwrap
import sys
import os
import time
import random

larguraTela = 200


# Configuração do Jogador

# TODO Criar um arquivo para cada classe

class Jogador:
    def __init__(self):
        self.nome = ''
        self.vida = 0
        self.mana = 0
        self.estado = []
        self.local = 'inicio'


meuJogador = Jogador()


# Tela de título
# TODO Criar um arquivo dentro da VIEWMODEL/VIEWCONTROLLER.
def telaDeSelecao():
    opcao = input("> ")
    if opcao.lower() == "play":
        jogar()
    elif opcao.lower() == "menu":
        menu()
    elif opcao.lower() == "quit":
        sys.exit()
    while opcao.lower() not in ['play', 'menu', 'quit']:
        print("Por favor digite um comando válido.")
        opcao = input("> ")
        if opcao.lower() == "play":
            jogar()
        elif opcao.lower() == "menu":
            menu()
        elif opcao.lower() == "quit":
            sys.exit()


# TODO Criar um arquivo separado na VIEW.
def tela():
    # os.system('cls')
    print('  ↬⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇼⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺↫')
    print('  |              ◐  Circus of Dark Madness ◑               |')
    print('  ╚►⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇼⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺◄╝')
    print('  §                                                         §')
    print('  §                         þlay                            §')
    print('  §                         ℳenu                           §')
    print('  §                         φuit                            §')
    print('  §                                                         §')
    print('  ╚►⇻⇻⇻⇻⇻⇻⇻⇻Creative commons © - 2022 - AZ0iC⇺⇺⇺⇺⇺⇺⇺⇺◄╝\n')
    telaDeSelecao()


# TODO Adicionar na VIEW.
def menu():
    print('  ↬⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇼⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺↫')
    print('  |               ◑ Circus of Dark Madness ◐               |')
    print('  ╚►⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇻⇼⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺⇺◄╝')
    print('  §                                                         §')
    print('  § Este jogo funciona com comandos escritos aprendidos     §')
    print('  § durante o jogo, ANOTE se quiser. A maioria dos comandos §')
    print('  § sera descrito, mas não custa nada tentar algo diferente.§')
    print('  § Boa sorte e não morra.                                  §')
    print('  ╚►⇻⇻⇻⇻⇻⇻⇻⇻Creative commons © - 2022 - AZ0iC⇺⇺⇺⇺⇺⇺⇺⇺◄╝\n')
    telaDeSelecao()


def jogar():
    pass  # placeholder


def movimentoJogador():
    pass  # placeholder


def interacaoJogador():
    pass  # placeholder


# TODO Criar um arquivo chamado linhaDoTempoModel
ZONA = ''
EXAMINAR = 'examinar'
DESCRICAO = 'descricao'
SOLUCIONADO = False
OPCAOA = '1', 'a', 'bom'
OPCAOB = '2', 'b', 'neutro bom'
OPCAOC = '3', 'c', 'neutro mal'
OPCAOD = '4', 'd', 'mal'

historia = {'inicio': False,
            'a1': False, 'b1': False, 'c1': False, 'd1': False,
            'a2': False, 'b2': False, 'c2': False, 'd2': False,
            'a3': False, 'b3': False, 'c3': False, 'd3': False,
            'a': False, 'b': False, 'c': False, 'd': False,
            }

# metodoAntigo = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
#                   'b1': False, 'b2': False, 'b3': False, 'b4': False,
#                   'c1': False, 'c2': False, 'c3': False, 'c4': False,
#                   } a progreção não é intuitiva


progressao = {
    # TODO Criar os finais A B C e D.
    'inicio': {
        ZONA: "Zona Inicial",
        EXAMINAR: "examinar",
        DESCRICAO: '''Veremos como fica a descrição     | 
  printada no terminal para regular | 
  a descrição e que fique bonita.  ''',
        SOLUCIONADO: False,
        OPCAOA: 'a1',
        OPCAOB: 'b1',
        OPCAOC: 'c1',
        OPCAOD: 'd1'
    },
    'a1': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a2',
        OPCAOB: 'b2',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b1': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a2',
        OPCAOB: 'b2',
        OPCAOC: 'c2',
        OPCAOD: ''
    },
    'c1': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b2',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'd1': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'a2': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a3',
        OPCAOB: 'b3',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b2': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a3',
        OPCAOB: 'b3',
        OPCAOC: 'c3',
        OPCAOD: ''
    },
    'c2': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b3',
        OPCAOC: 'c3',
        OPCAOD: 'd3'
    },
    'd2': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c2',
        OPCAOD: 'd2'
    },
    'a3': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: 'a',
        OPCAOB: '',
        OPCAOC: '',
        OPCAOD: ''
    },
    'b3': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: 'b',
        OPCAOC: '',
        OPCAOD: ''
    },
    'c3': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: 'c',
        OPCAOD: ''
    },
    'd3': {
        ZONA: "",
        EXAMINAR: "examinar",
        DESCRICAO: 'descricao',
        SOLUCIONADO: False,
        OPCAOA: '',
        OPCAOB: '',
        OPCAOC: '',
        OPCAOD: 'd'
    }
}

# sujeito a refatoração para retirada de prints e transformar em metodo de fato
def localizacao():
    print('\n' + ('#' * (4 + len(meuJogador.local))))
    print('# ' + meuJogador.local.upper() + ' #')
    print('| ' + progressao[meuJogador.local][DESCRICAO] + ' |')
    print('\n' + ('#' * (4 + len(meuJogador.local))))


def prompt():
    print("\n" + "=============================")
    print("O que você vai fazer?")
    acao = input("> ")

    acaoValida = [
        'mover',
        'ir',
        'viajar',
        'caminhar',
        'sair',
        'examinar',
        'inspecionar',
        'interagir',
        'olhar'
    ]
    while acao.lower() not in acaoValida:
        print('Ação desconhecida, tente novamente.\n')
        acao = input("> ")
    if acao.lower() == 'sair':
        sys.exit()
    elif acao.lower() in ['mover', 'ir', 'viajar', 'caminhar']:
        escolha(acao.lower())
    elif acao.lower() in ['examinar', 'inspecionar', 'interagir', 'olhar']:
        interacaoJogador()


def escolha():
    pergunta = "O que você vai fazer?"
    destino = input(pergunta)
    if destino.lower() in ['1', 'a', 'bom']:
        destinado = progressao[meuJogador.local][OPCAOA]
        manipuladorDeEscolhas()
    elif destino.lower() in ['2', 'b', 'neutro bom']:
        destinado = progressao[meuJogador.local][OPCAOB]
        manipuladorDeEscolhas()
    elif destino.lower() in ['3', 'c', 'neutro mal']:
        destinado = progressao[meuJogador.local][OPCAOB]
        manipuladorDeEscolhas()
    elif destino.lower() in ['4', 'd', 'mal']:
        destinado = progressao[meuJogador.local][OPCAOB]
        manipuladorDeEscolhas()


def manipuladorDeEscolhas(destinado):
    print("\n Você escolheu " + destinado + ".")
    meuJogador.local = destinado
    localizacao()


def jogadorExamina(acao):
    if progressao[meuJogador.local][SOLUCIONADO]:
        print("Ja solucionado")
    else:
        print("Deposite seu pussle aqui")


def iniciarJogo():
    return


tela()
