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

    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire en forme de losange.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.

        Note: 
            L'algorithme utilisé ici place aléatoirement les cartes dans la grille, en évitant de placer plusieurs fois la même carte dans une même cellule. 
            Cependant, il ne garantit pas une distribution parfaitement uniforme des cartes. Cet algorythme n'est pas optimisé non plus.
        """
        cards_dict = {}
        grid = []
        for card in range(cards):
            cards_dict[card] = 0
        for row in range(rows):
            grid += [[]]
            for column in range(columns):
                grid[row] += [[]]
        middle = int((len(grid[row])/2))
        while list(cards_dict.values()) != [4]*(cards):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if row <= middle:
                        if column >= middle and column <= middle+row:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                        elif column <= middle and column >= middle-row:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                    elif row > middle:
                        if column >= middle and column <= middle+(len(grid[row])-row):
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                        elif column <= middle and column >= middle-(len(grid[row])-row):
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
        return grid