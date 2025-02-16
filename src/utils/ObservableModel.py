# -*- coding: utf-8 -*-

###########################################
#                modules                  #
###########################################
from utils.ModelObserver import ModelObserver
###########################################

class ObservableModel():
    """Représente un modèle qui est observé/écouté.
    Args:
        observers: Liste des observeurs/écouteurs.
    """

    def __init__(self):
        self._observers:list = []

    def add_observer(self, m:ModelObserver) -> None:
        """Ajouter un observeur/écouteur.
        Args:
            o: object qui écoute.
        """
        self._observers.append(m)

    def remove_observer(self, m:ModelObserver) -> None:
        """Supprimer un observeur/écouteur.
        Args:
            o: object qui écoute.
        """
        self._observers.remove(m)

    def _fire_change(self) -> None:
        """Notifie ses observeurs/écouteurs d'un changement de la grille."""
        for observer in self._observers:
            observer.model_update(self)