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

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.
        """
        cards_dict = {}
        grid = []
        for card in range(cards):
            cards_dict[card] = 0
        for row in range(rows):
            grid += [[]]
            for column in range(columns):
                grid[row] += [[]]
        while list(cards_dict.values()) != [4]*(cards):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if row == 0 or row == len(grid)-1:
                        card = choice(list(cards_dict.keys()))
                        if cards_dict[card] != 4:
                            if len(grid[row][column]) == len(set(grid[row][column])):
                                cards_dict[card] += 1
                                grid[row][column].append(card)
                    elif column == 0 or column == len(grid[row])-1:
                        card = choice(list(cards_dict.keys()))
                        if cards_dict[card] != 4:
                            if len(grid[row][column]) == len(set(grid[row][column])):
                                cards_dict[card] += 1
                                grid[row][column].append(card)
        return grid