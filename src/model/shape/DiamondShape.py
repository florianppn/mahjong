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

class DiamondShape(ShapeStrategy):

    def generate_grid(self, rows: int, columns: int, cards: int):
        """Génère une grille de jeu aléatoire en forme de losange."""
        if rows < 2 or columns < 2 or cards < 2:
            raise ValueError("Lignes, colonnes et cartes doivent être supérieur à 2.")

        middle_row = rows // 2
        middle_column = columns // 2

        positions_top = [
            (i, j) for i in range(middle_row)
            for j in range(middle_column - i, middle_column + i + 1)
            for _ in range(4) #profondeur max.
            if 0 <= i < rows and 0 <= j < columns
            ]
        shuffle(positions_top)
        positions_bottom = [
            (i, j) for i in range(middle_row, rows)
            for j in range(middle_column - (rows - i - 1), middle_column + (rows - i - 1) + 1)
            for _ in range(4) #profondeur max.
            if 0 <= i < rows and 0 <= j < columns
            ]
        shuffle(positions_bottom)

        if cards*2 > len(positions_top)+len(positions_bottom):
            raise ValueError("Trop de cartes pour la taille du losange.")

        couples = [(i, i) for i in range(cards) for _ in range(3)]
        shuffle(couples)
        grid = [[[] for _ in range(columns)] for _ in range(rows)]
        for _ in range(len(positions_top)//2+len(positions_bottom)//2):
            couple = couples.pop()
            pos1, pos2 = positions_top.pop(), positions_bottom.pop()
            grid[pos1[0]][pos1[1]].append(couple[0])
            grid[pos2[0]][pos2[1]].append(couple[1])

        return grid

        