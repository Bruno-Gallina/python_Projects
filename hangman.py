# Hangman Game (Jogo da Forca)
#Programação Orientada a Objetos

# Import
import random

# Board (Tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Class (Classe)

class Hangman:

    #Método Construtor
    def __init__(self,word):



    #Método para advinhar a letra
    def guess(self, letter):


    #Método para verificar se o jogo terminou
    def hangman_over(self):


    #Método para verificar se o jogador venceu
    def hangman_won(self):


    #Método para não mostrar a letra no board
    def hide_word(self):


    #Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():


# Função Main - Execução do Programa
def main():


