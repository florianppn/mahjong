# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from copy import *
from random import choice
###########################################

###########################################
#                modules                  #
###########################################
from model.shape.ShapeStrategy import ShapeStrategy
from utils.ObservableModel import ObservableModel
###########################################

class Mahjong(ObservableModel):
    """Représente un modèle contenant une grille généré aléatoirement avec RandomGrid.

    Attributs:
        rows: Nombre de lignes de la grille.
        columns: Nombre de colonnes de la grille.
        cards: Nombre de cartes à placer dans la grille.
        shape: Forme de la grille.
        grid: grille généré aléatoirement.
        grid_copy: copie de la grille généré aléatoirement.
        move_history: Historique des coups joué par le joueur => (carte, (coordonnée de la première carte), (coordonnée de la deuxième carte)).
    """
    def __init__(self, rows:int, columns:int, cards:int, shape:ShapeStrategy):
        super().__init__()
        self.__rows, self.__columns = rows, columns
        self.__cards = cards
        self.__shape = shape
        self.__grid = shape.generate_grid(rows, columns, cards)
        self.__grid_copy = deepcopy(self.__grid)
        self.__move_history = []
        self.__cx, self.__cy = 64, 84
        self.__x0, self.__y0 = 55, 40
        self.__click1, self.__click2 = (), ()
        self.__remaining_cards = cards*4
        self.__shots = 0

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns

    def get_cards(self) -> int:
        return self.__cards

    def get_shape(self) -> ShapeStrategy:
        return self.__shape

    def get_grid(self) -> [[[int]]]:
        return self.__grid

    def get_grid_copy(self) -> [[[int]]]:
        return self.__grid_copy

    def get_move_history(self) -> [tuple]:
        return self.__move_history

    def get_click1(self) -> tuple:
        return self.__click1

    def get_click2(self) -> tuple:
        return self.__click2

    def get_cx(self) -> int:
        return self.__cx

    def get_cy(self) -> int:
        return self.__cy

    def get_x0(self) -> int:
        return self.__x0

    def get_y0(self) -> int:
        return self.__y0

    def get_remaining_cards(self) -> int:
        return self.__remaining_cards

    def get_shots(self) -> int:
        return self.__shots

    def set_grid(self, grid:[[[int]]]) -> None:
        self.__grid = grid
        self._fire_change()

    def set_grid_copy(self, grid_copy:[[[int]]]) -> None:
        self.__grid_copy = grid_copy
        self._fire_change()

    def set_rows(self, rows:int) -> None:
        self.__rows = rows
        self._fire_change()

    def set_columns(self, columns:int) -> None:
        self.__columns = columns
        self._fire_change()
    
    def set_cards(self, cards:int) -> None:
        self.__cards = cards
        self._fire_change()

    def set_shape(self, shape:ShapeStrategy) -> None:
        self.__shape = shape
        self._fire_change()

    def set_move_history(self, moves:[tuple]) -> None:
        self.__move_history = moves
        self._fire_change()

    def set_click1(self, t:tuple) -> None:
        self.__click1 = t
        self._fire_change()

    def set_click2(self, t:tuple) -> None:
        self.__click2 = t
        self._fire_change()

    def replay(self) -> None:
        """Jouer une nouvelle partie."""
        self.__grid = self.__shape.generate_grid(self.__rows, self.__columns, self.__cards)
        self.__grid_copy = deepcopy(self.__grid)
        self.__move_history = []
        self.__remaining_cards = self.__cards*4
        self.__shots = 0
        self._fire_change()

    def retry(self) -> None:
        """Rejouer la partie."""
        self.__grid = deepcopy(self.__grid_copy)
        self.__move_history = []
        self.__remaining_cards = self.__cards*4
        self.__shots = 0
        self._fire_change()

    def remove(self) -> None:
        """Supprimer un couple de cartes de la grille."""
        if self.__grid[self.__click1[0]][self.__click1[1]][0] == self.__grid[self.__click2[0]][self.__click2[1]][0] and self.__click1 != self.__click2:
            self.__move_history.append((self.__grid[self.__click1[0]][self.__click1[1]][0], (self.__click1), (self.__click2)))
            self.__grid[self.__click1[0]][self.__click1[1]].pop(0)
            self.__grid[self.__click2[0]][self.__click2[1]].pop(0)
            self.__remaining_cards -= 2
            self.__shots += 1
            self._fire_change()

    def add(self) -> None:
        """Ajout d'un couple de cartes dans la grille.
        Notes:
            - Ajout dans la grille des deux dernières cartes jouées si l'historique n'est pas vide.
            - Suppression dans l'historique des deux dernières cartes jouées si l'historique n'est pas vide.
            - Préviens les observeurs/écouteurs si l'historique n'est pas vide.
        """
        if self.__move_history != []:
            move = self.__move_history.pop()
            self.__grid[move[1][0]][move[1][1]].insert(0, move[0])
            self.__grid[move[2][0]][move[2][1]].insert(0, move[0])
            self.__remaining_cards += 2
            self.__shots -= 1
            self._fire_change()
    
    def is_empty(self) -> bool:
        """Vérifie si la grille est vide.
        Returns:
            - True si la grille est vide.
            - False si la grille est remplie.
        """
        return True if self.__remaining_cards == 0 else False

    def cards_position(self) -> list:
        """Obtenir une liste de toutes les cartes du jeu avec leur position.
        Returns:
            Une liste contenant des tuples qui contiennent le numéro de la carte, sa ligne et sa colonne.
        """
        return [(self.__grid[row][column][0], row, column) 
                for row in range(self.__rows) 
                for column in range(self.__columns)
                if len(self.__grid[row][column]) != 0]

    def playable_card_couple(self) -> [[tuple, tuple]]:
        """Obtenir une liste de tous les couples de cartes identiques pouvant être jouées.
        Returns:
            Une liste de listes, chaque sous-liste contenant deux tuples représentant un couple de cartes identiques.
        """
        positions = self.cards_position()
        position_couples = []
        uplets = []
        for i in range(len(positions)):
            uplets.append(positions[i])
            for i in range(len(positions)):
                if uplets[0][0] == positions[i][0]:
                    if uplets[0] != positions[i]:
                        if [(positions[i][1], positions[i][2]), (uplets[0][1], uplets[0][2])] not in position_couples:
                            position_couples.append([(uplets[0][1], uplets[0][2]), (positions[i][1], positions[i][2])])
            uplets = []
        return position_couples

    def is_blocked(self) -> bool:
        """Vérifie si la grille est bloquée.
        Returns:
            - True si la grille est bloquée.
            - False si la grille n'est pas bloquées.
        """
        couple_cards = self.playable_card_couple()
        for i in range(len(couple_cards)):
            if len(couple_cards[i]) > 1:
                return False
        return True

    def one_move(self) -> [tuple, tuple]:
        """Obtenir un couple de cartes identiques jouables.
        Returns:
            Une liste contenant deux tuples. Les tuples contiennent les coordonnées et le numéro des cartes identiques.
        """
        couples_cards = self.playable_card_couple()
        if (len(couples_cards) > 0):
            return choice(self.playable_card_couple())
        else:
            return None
