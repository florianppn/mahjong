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

class DoubleShape(ShapeStrategy):

    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire en forme de double rectangle.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.
        """
        couples = [(i, i) for i in range(cards) for _ in range(4)]
        shuffle(couples)
        grid = [[[] for _ in range(columns)] for _ in range(rows)]
        positions = [
            (i, j) for i in range(rows)
            for j in range(columns)
            for _ in range(4) #profondeur max.
            if (i == 0 or i == rows - 1) or (j == 0 or j == columns - 1) or \
            (i == 2 or i == rows - 3) and (j > 1 and j < columns - 2) or \
            (j == 2 or j == columns - 3) and (i > 1 and i < rows - 2)
            ]

        shuffle(positions)

        for i in range(len(positions)//2):
            couple = couples.pop()
            pos1, pos2 = positions.pop(), positions.pop()
            grid[pos1[0]][pos1[1]].append(couple[0])
            grid[pos2[0]][pos2[1]].append(couple[1])

        return grid