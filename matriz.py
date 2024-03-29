# Criando uma matriz bidimensional a partir do número de linhas e colunas oferecidos pelo usuário
# Importando a biblioteca Numpy

import numpy as np 
import random


class Matriz:
    def __init__(self):
        self.linhas = None
        self.colunas = None
        self.zeros = None
        self.uns = None
        self.matriz = []

    def get_input(self):
        print("Insira os dados:")
        # Variável para informar o número de linhas e colunas da matriz.
        self.linhas = int(input("Linhas: "))
        self.colunas = int(input("Colunas: "))
        self.matriz = np.zeros((self.linhas, self.colunas))  # Gerando uma matriz com valores iniciais igual a 0.
        return self.matriz
    
    # Loop para substituir o número 0 por 1.
    def replace(self):
        for _ in range(random.randint(0, 600)): 
            total_linhas = np.random.randint(0, self.linhas)
            total_colunas = np.random.randint(0, self.colunas)
            # Substitui o elemento na posição aleatória que inicia com 0 por 1.
            self.matriz[total_linhas, total_colunas] = 1
        return self.matriz
    
    # Contando o número de zeros e uns na matriz.
    def getZero(self):
        self.zeros = np.count_nonzero(self.matriz == 0)
        return f'Número de zeros na matriz: {self.zeros}'
    
    def getUns(self):
        self.uns = np.count_nonzero(self.matriz == 1)
        return f'Número de uns na matriz: {self.uns}'
