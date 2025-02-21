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

class RectangleShape(ShapeStrategy):

    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire en forme de rectangle.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.
        """
        couples = [(i, i) for i in range(cards) for _ in range(4)]
        shuffle(couples)
        grid = [[[] for _ in range(columns)] for _ in range(rows)]
        positions = [
            (i, j) for i in range(rows)
            for j in range(columns)
            for _ in range(4) #profondeur max.
            if (i == 0 or i == rows-1) or (j == 0 or j == columns-1)
            ]

        shuffle(positions)

        for i in range(len(positions)//2):
            couple = couples.pop()
            pos1, pos2 = positions.pop(), positions.pop()
            grid[pos1[0]][pos1[1]].append(couple[0])
            grid[pos2[0]][pos2[1]].append(couple[1])

        return grid