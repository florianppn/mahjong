# -*- coding: utf-8 -*-

###########################################
#                librairies               #
###########################################
from abc import ABC, abstractmethod
###########################################

class ShapeStrategy(ABC):
    """Représente une forme de grille."""

    @abstractmethod
    def generate_grid(self, rows:int, columns:int, cards:int):
        """Génère une grille de jeu aléatoire en forme de donut.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
            cards: Nombre de cartes à placer dans la grille.

        Returns:
            Une liste de listes qui contiennent des listes d'entiers représentant la grille générée aléatoirement. Chaque élément de la liste interne correspond à une carte.
        """
        pass