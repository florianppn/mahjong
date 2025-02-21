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
        if rows < 2 or columns < 2 or cards < 2:
            raise ValueError("Lignes, colonnes et cartes doivent être supérieur à 2.")

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

        if len(couples)*2 <= len(positions):
            raise ValueError("Pas assez de cartes !")

        for i in range(len(positions)//2):
            couple = couples.pop()
            pos1, pos2 = positions.pop(), positions.pop()
            grid[pos1[0]][pos1[1]].append(couple[0])
            grid[pos2[0]][pos2[1]].append(couple[1])

        return grid