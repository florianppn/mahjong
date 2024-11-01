# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
import os
###########################################

###########################################
#                modules                  #
###########################################
from model.ModelObserver import ModelObserver
###########################################

class ViewMainMenu(Frame, ModelObserver):
    """Représente la vue du menu principal.
    Args:
        tk: Interface mère du jeu.
        controller: Contrôleur du jeu.
        resume: bouton pour lancer une sauvegarde si elle existe.
        buttons: Liste des boutons de couleurs.
    """
    
    def __init__(self, tk:Tk, controller):
        super().__init__(tk)
        ModelObserver().__init__()
        self.pack()
        self.__tk = tk
        self.__controller = controller

        self.__resume = None
        self.__buttons = []
        self.configure_view_buttons()
        self.configure_control_button()

    def configure_control_button(self) -> None:
        """Création d'un bouton de contrôle pour la vue.
        Notes:
            - Création du bouton quitter avec une fonction associée.
        """
        button = Button(self, text = "Quit", command = lambda : (self.__tk.quit(), self.__tk.destroy()))
        button.config(font = ("comic",10,"bold"), bg="white", activebackground = "red3")
        button.grid(row = 2, column = 1, padx = 40, pady = 20, ipadx = 50)

    def configure_view_buttons(self) -> None:
        """Création des boutons permettant de naviguer entre les différentes vues.
        Notes:
            - il existe 4 autres vues : Demo mode, Classic mode, Color settings et Grid settings.
            - Resume ne fait que charger une partie de mahjong avec la grille sauvegardée.
        """
        data = [("Demo mode", lambda : None, (0, 2)),
                ("Classic mode", lambda : self.__controller.show_game(False), (1, 2)),
                ("Resume", lambda : self.__controller.show_game(True), (2, 2)),
                ("Color settings", lambda : self.__controller.show_color_menu(), (0, 1)),
                ("Grid settings", lambda : self.__controller.show_grid_menu(), (1, 1))]
        for text, command, (row, column) in data:
            button = Button(self, text = text, command = command)
            button.config(font = ("comic", 10, "bold"))
            button.grid(row = row, column = column, padx = 40, pady = 20, ipadx = 20)
            self.__buttons.append(button)
            if text == "Resume":
                self.__resume = button

    def model_update_theme(self, theme:str) -> None:
        """Mise à jour de la couleur de l'arrière plan par le modèle.
        Args:
            theme: nouvelle couleur de l'arrière plan.
        Notes:
            - à lieu lors d'un changement de couleur.
        """        
        self.__tk.config(bg=theme)
        self.config(bg=theme)

    def model_update_colors(self, theme:str, bg:str, fg:str, activebackground:str, activeforeground:str) -> None:
        """Mise à jour pour la vue par le modèle.
        Args:
            theme: couleur de l'arrière plan.
            bg: couleur de fond d'un bouton.
            fg: couleur du texte d'un bouton.
            activebackground: couleur du fond d'un bouton lors du passage de la souris.
            activeforeground: couleur du texte d'un bouton lors du passage de la souris.
        Notes:
            - à lieu lors de la mise en route du jeu.
        """
        self.__tk.config(bg=theme)
        self.config(bg=theme)
        for button in self.__buttons:
            button.config(bg=bg, fg=fg, activebackground=activebackground, activeforeground=activeforeground)

    def active_resume(self) -> None:
        """Active le clic sur le bouton Resume.
        Notes:
            - Utile s'il y a une sauvegarde.
        """
        self.__resume.config(state = NORMAL)

    def deactivate_resume(self) -> None:
        """Désactive le clic sur le bouton Resume.
        Notes:
            - Utile s'il n'y a pas de sauvegarde.
        """
        self.__resume.config(state = DISABLED)
