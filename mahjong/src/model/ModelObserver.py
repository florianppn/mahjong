# -*- coding: utf-8 -*-

class ModelObserver():
    """Représente un observeur/écouteur."""

    def model_update(self, o:object) -> None:
        """Mise à jour de l'observeur.
        Args:
            grid: grille du jeu.
        Raises:
            NotImplementedError: Si la méthode est appelé mais n'est pas implémenté.
        """
        raise NotImplementedError

    def model_update_theme(self, theme:str) -> None:
        """Mise à jour de la couleur de l'arrière plan des différentes vues.
        Args:
            theme: nouvelle couleur des différentes vues.
        Raises:
            NotImplementedError: Si la méthode est appelé mais n'est pas implémenté.
        """
        raise NotImplementedError

    def model_update_colors(self, theme:str, bg:str, fg:str, activebackground:str, activeforeground:str) -> None:
        """Mise à jour des couleurs des différents éléments du jeu (boutons, titres, thème, etc...).
        Args:
            theme: couleur de fond du jeu.
            bg: couleur de fond d'un bouton.
            fg: couleur du texte d'un bouton.
            activebackground: couleur du fond d'un bouton lors du passage de la souris.
            activeforeground: couleur du texte d'un bouton lors du passage de la souris.
        Raises:
            NotImplementedError: Si la méthode est appelé mais n'est pas implémenté.
        """
        raise NotImplementedError