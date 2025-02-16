# -*- coding: utf-8 -*-

###########################################
#                librairies               #
###########################################
from abc import ABC, abstractmethod
###########################################

class ModelObserver(ABC):
    """Représente un observeur/écouteur."""

    @abstractmethod
    def model_update(self, o:object) -> None:
        """Mise à jour de l'observeur.
        Args:
            grid: grille du jeu.
        Raises:
            NotImplementedError: Si la méthode est appelé mais n'est pas implémenté.
        """
        pass