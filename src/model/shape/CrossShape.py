# -*- coding: utf-8 -*-

###########################################
#                librairies               #
###########################################
from random import *
###########################################

###########################################
#                modules                  #
###########################################
from model.shape.ShapeStrategy import ShapeStrategy
###########################################

class CrossShape(ShapeStrategy):

    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire en forme de croix.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.
        """
        middle_row = rows//2
        middle_column = columns//2
        grid = [[[] for _ in range(columns)] for _ in range(rows)]
        couples = [(i, i) for i in range(cards) for _ in range(3)]
        positions = [
            (i, j) for i in range(rows) 
            for j in range(columns) 
            for _ in range(4) #profondeur max.
            if (i == middle_row or i == middle_row-1) or (j == middle_column or j == middle_column-1)
            ]
        shuffle(couples)
        shuffle(positions)
        for i in range(len(positions)//2):
            couple = couples.pop()
            pos1, pos2 = positions.pop(), positions.pop()
            grid[pos1[0]][pos1[1]].append(couple[0])
            grid[pos2[0]][pos2[1]].append(couple[1])
        return grid
