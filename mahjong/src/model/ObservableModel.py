# -*- coding: utf-8 -*-

###########################################
#                modules                  #
###########################################
from model.ModelObserver import ModelObserver
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

    def _notify_grid_change(self) -> None:
        """Notifie ses observeurs/écouteurs d'un changement de la grille."""
        for observer in self._observers:
            observer.model_update(self)

    def _notify_theme_change(self, theme:str) -> None:
        """Notifie ses observeurs/écouteurs d'un changement de couleur du thème."""
        for observer in self._observers:
            observer.model_update_theme(theme)

    def _notify_colors_change(self, theme:str, bg:str, fg:str, activebackground:str, activeforeground:str) -> None:
        """Notifie ses observeurs/écouteurs d'un changement des couleurs des différents éléments du jeu (boutons, titres, thème, etc...)."""
        for observer in self._observers:
            observer.model_update_colors(theme, bg, fg, activebackground, activeforeground)