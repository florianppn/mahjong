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

class ViewGridMenu(Frame, ModelObserver):
    """Représente la vue de configuration de la grille.
    Args:
        tk: Interface mère du jeu.
        controller: Contrôleur du jeu.
        entry_rows: L'entrée contenant le nombre de lignes.
        entry_columns: L'entrée contenant le nombre de colonnes.
        entry_cards: L'entrée contenant le nombre de cartes.
        button_size: Bouton pour valider la taille de la grille.
        button_cards: Bouton pour valider le nombre de cartes dans la grille.
        popup_size: Label pour taille de grille.
        popup_cards: Label pour nombre de cartes.
        buttons: Liste des boutons pour les différentes formes de la grille.
        labels: Liste de labels contenant les différents labels présents sur la vue.
        frames: Liste des frames contenant les différentes frames présents sur la vue.
    """

    def __init__(self, tk:Tk, controller):
        super().__init__(tk)
        ModelObserver().__init__()
        self.forget()
        self.__tk = tk
        self.__controller = controller

        self.__entry_rows = None
        self.__entry_columns = None
        self.__entry_cards = None
        self.__button_size = None
        self.__button_cards = None
        self.__popup_size = None
        self.__popup_cards = None

        self.__buttons = []
        self.__labels = []
        self.__frames = []
        container1 = self.configure_main_frame("Configure the classic shape grid :")
        container2 = self.configure_main_frame("Other grids of different shapes :")
        self.configure_size_inputs(container1)
        self.configure_cards_input(container1)
        self.configure_shape_buttons(container2)
        self.configure_control_buttons()

    def configure_main_frame(self, text:str) -> Frame:
        """Création de la frame principale.
        Args:
            text: titre du Label.
        Returns:
            Une Frame contenant un label.
        """
        container = Frame(self)
        container.config(highlightbackground="black", highlightcolor="black", highlightthickness=2)
        container.pack(side = TOP, pady = 20, padx = 10)
        label = Label(container, text = text)
        label.config(font = ("comic", 10, "bold"))
        label.pack(side = TOP, padx = 10, pady = 20)
        self.__labels.append(label)
        self.__frames.append(container)
        return container

    def configure_size_inputs(self, frame:Frame) -> None:
        """Création du système de configuration pour le nombre de lignes et le nombre de colonnes de la grille.
        Args:
            frame: Cadre dans lequel se situera la configuration.
        Notes:
            - Contient les entrées, les boutons et les popups liées à configuration la taille de la grille.
        """
        grid_size = Frame(frame)
        grid_size.pack(side = TOP, pady = 20, padx = 10)
        self.__frames.append(grid_size)
        popup = Frame(frame)
        popup.pack(side = TOP)
        self.__frames.append(popup)
        for text in ["rows", "columns"]:
            label = Label(grid_size, text = text)
            label.config(font = ("comic", 10, "bold"))
            label.pack(side = LEFT)
            self.__labels.append(label)
            entry_tmp = Entry(grid_size)
            entry_tmp.config(font = ("comic", 10, "bold"))
            entry_tmp.pack(side = LEFT)
            if text == "rows":
                self.__entry_rows = entry_tmp
            elif text == "columns":
                self.__entry_columns = entry_tmp
        self.__button_size = Button(grid_size,text = "OK",command = lambda : self.__controller.is_valid_size(self.__entry_rows.get(), self.__entry_columns.get()))
        self.__button_size.config(font = ("comic", 10, "bold"), bg="white")
        self.__button_size.pack(side = LEFT, padx = 10)
        self.__popup_size = Label(popup, text = "You must put a number between 4 and 8", fg = "red3")
        self.__popup_size.config(font = ("comic", 10, "bold"))
        self.__popup_size.pack_forget()

    def configure_cards_input(self, frame:Frame) -> None:
        """Création du système de configuration pour le nombre de cartes.
        Args:
            frame: Cadre dans lequel se situera la configuration.
        Notes:
            - Contient les entrées, les boutons et les popups liées à configuration la taille de la grille.
        """
        grid_cards = Frame(frame)
        grid_cards.pack(side = TOP, pady = 20, padx = 10)
        self.__frames.append(grid_cards)
        popup = Frame(frame)
        popup.pack(side = TOP)
        self.__frames.append(popup)
        label = Label(grid_cards, text = "cards")
        label.config(font = ("comic", 10, "bold"))
        label.pack(side = LEFT)
        self.__labels.append(label)
        self.__entry_cards = Entry(grid_cards)
        self.__entry_cards.config(font = ("comic", 10, "bold"))
        self.__entry_cards.pack(side = LEFT)
        self.__button_cards = Button(grid_cards, text = "OK", command = lambda : self.__controller.is_valid_cards(self.__entry_cards.get()))
        self.__button_cards.config(font = ("comic", 10, "bold"), bg="white")
        self.__button_cards.pack(side = LEFT, padx = 10)
        self.__popup_cards = Label(popup, text = "You must put a number between 10 and 24", fg = "red3")
        self.__popup_cards.config(font = ("comic", 10, "bold"))
        self.__popup_cards.pack_forget()

    def configure_control_buttons(self) -> None:
        """Création des boutons de contrôle pour la vue.
        Notes:
            - Création du bouton quitter avec une fonction associée.
            - Création du bouton menu avec une fonction associée.
        """
        data = [("Quit", lambda: (self.quit(), self.destroy()), "red3", LEFT), ("Menu", lambda: self.__controller.show_menu("grid_menu"), "dodger blue", RIGHT)]
        for text, command, activecolor, side in data:
            button = Button(self, text=text, command=command)
            button.config(font=("comic", 10, "bold"), bg="white", activebackground=activecolor)
            button.pack(side=side, padx=10, pady=10)

    def configure_shape_buttons(self, frame:Frame) -> None:
        """Création des boutons pour les différentes formes de la grille.
        Args:
            frame: Cadre dans lequel se situera la configuration.
        Notes:
            - 6 formes de grille disponible.
        """
        grid_shape = Frame(frame)
        grid_shape.pack(side = TOP, pady = 20, padx = 10)
        self.__frames.append(grid_shape)
        shapes = ["Rectangle", "Diamond", "Double", "Donut", "Cross", "classic"]
        positions = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
        for shape, position in zip(shapes, positions):
            self.configure_shape_button(shape, position, grid_shape)

    def configure_shape_button(self, shape:str, position:tuple, frame:Frame) -> None:
        """Création d'un bouton pour une forme de grille.
        Args:
            shape: forme de la grille.
            position: position du bouton dans le cadre.
            frame: cadre contenant le bouton.
        """
        button = Button(frame, text=shape, width=10, height=2, command = lambda : self.__controller.grid_shape(shape.lower()))
        button.config(font = ("comic", 10, "bold"))
        button.grid(row = position[0], column = position[1], padx = 5, pady = 5)
        self.__buttons.append(button)

    def model_update_theme(self, theme:str) -> None:
        """Mise à jour de la couleur de l'arrière plan par le modèle.
        Args:
            theme: nouvelle couleur de l'arrière plan.
        Notes:
            - à lieu lors d'un changement de couleur.
        """
        self.config(bg=theme)
        self.__popup_size.config(bg=theme)
        self.__popup_cards.config(bg=theme)
        for label in self.__labels:
            label.config(bg=theme)
        for frame in self.__frames:
            frame.config(bg=theme)

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
        self.__popup_size.config(bg=theme)
        self.__popup_cards.config(bg=theme)
        for button in self.__buttons:
            button.config(bg=bg, fg=fg, activebackground=activebackground, activeforeground=activeforeground)
        for label in self.__labels:
            label.config(bg=theme)
        for frame in self.__frames:
            frame.config(bg=theme)

    def active_buttons(self) -> None:
        """Active le clic sur les boutons de confirmation pour la taille et le nombre de cartes dans une grille.
        Notes:
            - Utile si c'est une grille de forme classique.
        """
        self.__button_size.config(state = NORMAL)
        self.__button_cards.config(state = NORMAL)

    def deactivate_buttons(self) -> None:
        """Désactive le clic sur les boutons de confirmation pour la taille et le nombre de cartes dans une grille.
        Notes:
            - Utile si c'est une grille spéciale (différente de la forme classique).
        """
        self.__button_size.config(state = DISABLED)
        self.__button_cards.config(state = DISABLED)

    def active_popup_grid_size(self) -> None:
        """Active la popup pour la taille de la grille.
        Notes:
            - Utile si la taille n'est pas conforme.
        """
        self.__popup_size.pack()

    def deactivate_popup_grid_size(self) -> None:
        """Désactive la popup pour la taille de la grille.
        Notes:
            - Utile si la taille est conforme.
        """
        self.__popup_size.forget()
        self.__entry_rows.delete(0, END)
        self.__entry_columns.delete(0, END)

    def active_popup_text_cards(self) -> None:
        """Active la popup pour le nombre de cartes dans la grille.
        Notes:
            - Utile si le nombre de cartes n'est pas conforme.
        """
        self.__popup_cards.pack()

    def deactivate_popup_text_cards(self) -> None:
        """Désactive la popup pour le nombre de cartes dans la grille.
        Notes:
            - Utile si le nombre de cartes est conforme.
        """
        self.__popup_cards.forget()
        self.__entry_cards.delete(0, END)
