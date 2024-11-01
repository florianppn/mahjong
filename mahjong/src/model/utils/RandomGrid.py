# -*- coding: utf-8 -*-

###########################################
#                librairies               #
###########################################
from random import *
###########################################

class RandomGrid:
    """ Permet de générer des grilles de jeu aléatoirement."""

    def generate_random_grid(self, rows:int, columns:int, cards:int, shape:str=None) -> [[[int]]]:
        """Génère une grille de jeu aléatoire de taille spécifiée, avec un nombre donné de cartes et une forme optionnelle.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.
            shape: Forme de la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers, cela représente la grille générée aléatoirement. Chaque entier correspond à une carte.
        """
        if shape == "rectangle":
            return self.random_grid_rectangle(8, 8, 34)
        elif shape == "double":
            return self.random_grid_double(8, 8, 34)
        elif shape == "cross":
            return self.random_grid_cross(8, 8, 34)
        elif shape == "diamond":
            return self.random_grid_diamond(8, 7, 34)
        elif shape == "donut":
            return self.random_grid_donut(8, 8, 34)
        else:
            return self.random_grid(rows, columns, cards)

    def random_grid(self, rows:int, columns:int, cards:int) -> [[[int]]]:
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

    def random_grid_rectangle(self, rows, columns, cards):
        """Génère une grille de jeu aléatoire en forme de rectangle.
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

    def random_grid_double(self, rows, columns, cards):
        """Génère une grille de jeu aléatoire en forme de double rectangle.
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
                    elif row == 2 or row == len(grid)-3:
                        if column > 1 and column < len(grid)-2:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                    elif column == 2 or column == len(grid[row])-3:
                        if row > 1 and row < len(grid[row])-2:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                                
        return grid

    def random_grid_cross(self, rows, columns, cards):
        """Génère une grille de jeu aléatoire en forme de croix.
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
        while list(cards_dict.values()) != [4]*(cards):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if row < len(grid)-5 or row > len(grid)-4:
                        if column == len(grid[row])-5 or column == len(grid[row])-4:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                    elif row == len(grid)-5 or row == len(grid)-4:
                        card = choice(list(cards_dict.keys()))
                        if cards_dict[card] != 4:
                            if len(grid[row][column]) == len(set(grid[row][column])):
                                cards_dict[card] += 1
                                grid[row][column].append(card)
        return grid

    def random_grid_diamond(self, rows,columns,cards):
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

    def random_grid_donut(self, rows,columns,cards):
        """Génère une grille de jeu aléatoire en forme de donut.
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
                    elif row == 1 or row == len(grid)-2:
                        if column > 0 and column < len(grid)-1:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)
                    elif column == 1 or column == len(grid[row])-2:
                        if row > 0 and row < len(grid[row])-1:
                            card = choice(list(cards_dict.keys()))
                            if cards_dict[card] != 4:
                                if len(grid[row][column]) == len(set(grid[row][column])):
                                    cards_dict[card] += 1
                                    grid[row][column].append(card)     
        return grid

