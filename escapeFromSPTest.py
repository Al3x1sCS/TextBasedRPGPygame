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


meuJogador = Jogador()

# Tela de título

def telaDeSelecao():
    opcao = input("> ")
    if opcao.lower() == ("Jogar"):
        comecarJogo() # Placeholder

