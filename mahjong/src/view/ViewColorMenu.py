# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.ModelObserver import ModelObserver
###########################################

class ViewColorMenu(Frame, ModelObserver):
    """Répresente la vue du menu couleur.
    Args:
        tk: Interface mère du jeu.
        controller: Contrôleur du jeu.
        buttons: Liste des boutons de couleurs.
        title: Label du menu.
    Notes:
        - Le panel des différentes couleurs de Tkinter sont disponibles ici : https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
    """

    def __init__(self, tk:Tk, controller):
        super().__init__(tk)
        ModelObserver().__init__()
        self.forget()
        self.__tk = tk
        self.__controller = controller

        self.__buttons = []
        self.__title = self.configure_main_label("Changes the game background color")
        self.configure_color_buttons()
        self.configure_control_buttons()

    def configure_main_label(self, text:str) -> Label:
        """Création du Label principal.
        Args:
            text: titre du label.
        Returns:
            un Label.
        """
        label = Label(self, text = text)
        label.config(font = ("comic", 10, "bold"))
        label.grid(row = 0, column = 2, columnspan = 2, padx = 10, pady = 20)
        return label

    def configure_control_buttons(self) -> None:
        """Création des boutons de contrôle pour la vue.
        Notes:
            - Création du bouton quitter avec une fonction associée.
            - Création du bouton menu avec une fonction associée.
        """
        data = [("Quit", lambda: (self.quit(), self.destroy()), "red3", (5, 0)), ("Menu", lambda: self.__controller.show_menu("color_menu"), "dodger blue", (5, 5))]
        for text, command, activecolor, (row, column) in data:
            button = Button(self, text=text, command=command)
            button.config(font=("comic", 10, "bold"), bg="white", activebackground = activecolor)
            button.grid(row = row, column = column, padx = 10, pady = 10)

    def configure_color_buttons(self) -> None:
        """Création des boutons de couleurs pour la vue.
        Notes:
            - 17 couleurs disponibles.
        """
        colors = [
            "white", "forest green", "slate blue", "royal blue",
            "LightSteelBlue1", "plum1", "SeaGreen3", "LightSalmon2",
            "cyan4", "brown3", "tomato4", "MediumPurple1",
            "DarkOliveGreen3", "LightGoldenrod2", "gray30", "pale green"]
        button_positions = [
            (1, 1), (2, 1), (3, 1), (4, 1),
            (1, 2), (2, 2), (3, 2), (4, 2),
            (1, 3), (2, 3), (3, 3), (4, 3),
            (1, 4), (2, 4), (3, 4), (4, 4),]
        for color, position in zip(colors, button_positions):
            self.configure_color_button(color, position)
    
    def configure_color_button(self, color, position) -> None:
        """Création d'un bouton de couleur personalisé pour la vue.
        Args:
            color: nom de la couleur associé au bouton.
            position: position du bouton sur la vue.
        """
        button = Button(self, text=color, width=15, height=2, command = lambda : self.__controller.set_theme_color(color))
        button.config(font = ("comic", 10, "bold"))
        button.grid(row = position[0], column = position[1], padx = 5, pady = 10)
        self.__buttons.append(button)

    def model_update_theme(self, theme:str) -> None:
        """Mise à jour de la couleur de l'arrière plan par le modèle.
        Args:
            theme: nouvelle couleur de l'arrière plan.
        Notes:
            - à lieu lors d'un changement de couleur.
        """
        self.config(bg = theme)
        self.__title.config(bg = theme)

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
        self.config(bg=theme)
        self.__title.config(bg=theme)
        for button in self.__buttons:
            button.config(bg=bg, fg=fg, activebackground=activebackground, activeforeground=activeforeground)