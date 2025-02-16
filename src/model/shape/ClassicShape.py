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

        Note: 
            L'algorithme utilisé ici place aléatoirement les cartes dans la grille, en évitant de placer plusieurs fois la même carte dans une même cellule. 
            Cependant, il ne garantit pas une distribution parfaitement uniforme des cartes. Cet algorythme n'est pas optimisé non plus.
        """
        cards_list = []
        cnt = 0
        grid = []
        for card in range(cards):
            cards_list += [card]
        for row in range(rows):
            grid += [[]]
            for column in range(columns):
                grid[row] += [[]]
        while cnt < len(cards_list):
            for i in range(4):
                i = randint(0, rows-1)
                j = randint(0, columns-1)
                while grid[i][j] == [cnt, cnt]:
                    i = randint(0, rows-1)
                    j = randint(0, columns-1)
                grid[i][j].append(cards_list[cnt])
            cnt += 1
        return grid