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

class ClassicShape(ShapeStrategy):

    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.
        """
        depth = 4
        cards = [i for i in range(cards) for _ in range(depth)]
        grid = [[[] for _ in range(rows)] for _ in range(columns)]
        positions = [(i, j) for i in range(rows) for j in range(columns)]
        shuffle(positions)
        shuffle(cards)
        for i in range(len(cards)):
            pos = positions[0]
            if len(grid[pos[0]][pos[1]]) >= (depth-1):
                positions.pop(0)
            grid[pos[0]][pos[1]].append(cards.pop())
        return grid