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
from model.Grid import Grid
from model.GameSettings import GameSettings
from view.ViewGame import ViewGame
from view.ViewMainMenu import ViewMainMenu
from view.ViewColorMenu import ViewColorMenu
from view.ViewGridMenu import ViewGridMenu
from model.utils.JsonLoader import JsonLoader
###########################################

class ControllerGame:
    """Répresente le contrôleur du jeu.
    Args:
        root: Interface mère du jeu (Tk).
        view_game: Vue d'une partie de mahjong (Frame).
        view_menu: Vue du menu principal du jeu (Frame).
        view_color_menu: Vue du menu des couleurs du jeu (Frame).
        view_grid_menu: Vue du menu des paramètres de la grille mahjong (Frame).
        grid: Modèle contenant la grille du jeu.
        game_settings: Modèle contenant les paramètres du jeu.
        click1: Position du premier click lors d'une partie de Mahjong.
        click2: Position du deuxième click lors d'une partie de Mahjong.
    """
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Mahjong")
        self.__root.geometry("810x810") 
        self.__view_game = ViewGame(self.__root, self)
        self.__view_menu = ViewMainMenu(self.__root, self)
        self.__view_color_menu = ViewColorMenu(self.__root, self)
        self.__view_grid_menu = ViewGridMenu(self.__root, self)
        self.__grid = Grid()
        self.__game_settings = GameSettings()
        self.__click1 = ()
        self.__click2 = ()

    def run(self) -> None:
        """Démarrer le jeu.
        Notes:
            - Ajoute les différents observeurs/écouteurs aux différents modèles.
            - Active/désactive le bouton "Resume" du menu principal si une sauvegarde existe ou non.
            - Lance l'interface mère et toutes ses filles.
        """
        self.__grid.add_observer(self.__view_game)
        self.__game_settings.add_observer(self.__view_game)
        self.__game_settings.add_observer(self.__view_menu)
        self.__game_settings.add_observer(self.__view_color_menu)
        self.__game_settings.add_observer(self.__view_grid_menu)
        self.__game_settings.forced_loading()
        if os.path.exists("../data/save/save"):
            self.__view_menu.active_resume()
        else:
            self.__view_menu.deactivate_resume()
        self.__root.mainloop()

    def show_menu(self, origin:str) -> None:
        """Montrer le menu en fonction de l'origine de la demande.
        Args:
            origin: Vue qui demande le retour au menu principal.
        Raises:
            Exception: Si une demande de retour n'existe pas.
        """
        if origin == "color_menu":
            self.__view_color_menu.forget()
        elif origin ==  "game":
            self.__view_game.deactivate_bind()
            self.__view_game.forget()
        elif origin == "grid_menu":
            self.__view_grid_menu.forget()
        else:
            raise Exception("There was an error changing frame")
        self.__view_menu.pack() #pack permet ici de montrer la vue sur le menu principal contrairement à forget qui permet de la cacher.

    def show_grid_menu(self) -> None:
        """Montrer le menu grille."""
        self.__view_menu.forget()
        self.is_classic_grid()
        self.__view_grid_menu.pack()

    def show_color_menu(self) -> None:
        """Montrer le menu des couleurs."""
        self.__view_menu.forget()
        self.__view_color_menu.pack()

    def show_game(self, back_up:bool) -> None:
        """Montrer une partie de Mahjong.
        Args:
            back_up: si la grille doit charger une sauvegarde ou générer une nouvelle grille.
        """
        self.__view_menu.forget()
        self.__view_game.pack()
        self.__grid.load_grid(True) if back_up else self.__grid.load_grid(False)
        self.__view_game.end_text()
        self.__view_game.active_bind()

    def play_again(self) -> None:
        """Jouer une nouvelle partie."""
        self.__grid.replay()
        self.__view_game.active_bind()
        self.__view_game.end_text()
        self.__view_game.buttons_state()

    def try_again(self) -> None:
        """Rejouer la partie avec la même grille."""
        self.__grid.retry()
        self.__view_game.active_bind()
        self.__view_game.end_text()
        self.__view_game.buttons_state()

    def ending(self) -> None:
        """Fin du jeu.
        Notes:
            - Si le status de fin n'est pas vide alors on lance la fin du jeu.
            - Fin du jeu dans deux cas => (1): grille vide (2): plus de couples identiques dans la grille.
        """
        status = self.__grid.end()
        if status != "":
            self.__view_game.deactivate_bind()
            self.__view_game.end_text(status)
            self.__view_game.buttons_state(False)

    def find_playable_card(self) -> None:
        """Trouver une carte jouable.
        Notes:
            - Une carte jouable est une carte faisant partie d'un couple de cartes identiques.
        """
        self.__click1 = ()
        self.__click2 = ()
        move = self.__grid.one_move()
        self.__view_game.show_card(move[0][0], move[0][1], self.__grid.get_grid())
    
    def find_playable_card_couple(self) -> None:
        """Trouver un couple de cartes jouables.
        Notes:
            - Un couple de cartes jouables est un couple de cartes identiques.
        """
        self.__click1 = ()
        self.__click2 = ()
        move = self.__grid.one_move()
        self.__view_game.show_card_couple(move[0][0], move[0][1], move[1][0], move[1][1], self.__grid.get_grid())

    def backspace(self) -> None:
        """Retour en arrière de la grille de jeu.
        Notes:
            - Lors d'un mouvement non désiré il est possible de retourner en arrière, d'effacer le mouvement.
        """
        self.__grid.add()

    def is_clickable(self, event) -> bool:
        """Vérifie si une case de l'interface graphique du Mahjong est cliquable.
        Returns:
            Vrai si le clic a été effectué sur une carte sinon Faux.
        """
        x0, y0 = self.__view_game.get_x0(), self.__view_game.get_y0()
        cx, cy = self.__view_game.get_cx(), self.__view_game.get_cy()
        rows, columns = self.__grid.get_rows(), self.__grid.get_columns()
        i, j = (event.y-y0)//cy, (event.x-x0)//cx #transforme les coordonnées du clic en indices de ligne et de colonne pour la grille de jeu. 
        if i in range(rows) and j in range(columns):
            self.__click1, self.__click2 = self.__view_game.to_click(i, j, rows, columns, self.__grid.get_grid(), self.__click1, self.__click2)
            return True
        return False

    def make_move(self, click1:tuple, click2:tuple) -> None:
        """Supprime le couple de cartes identiques.
        Args:
            click1: clic sur la première carte.
            click2: clic sur la deuxième carte.
        """
        self.__grid.remove(click1, click2)

    def back_up(self) -> None:
        """Sauvegarde de la grille de jeu."""
        self.__grid.save_grid()

    def set_theme_color(self, color:str) -> None:
        """Modification de la couleur du jeu.
        Args:
            color: nom de la nouvelle couleur.
        """
        self.__game_settings.set_color_theme(color)

    def is_classic_grid(self) -> bool:
        """Vérifie si la grille de jeu est au format classique.
        Notes:
            - Utile pour le menu de paramétrage de la grille.
            - Permet la désactivation des buttons pour choisir la taille/nombre de cartes de la grille.
        """
        if self.__game_settings.get_shape() == "classic":
            self.__view_grid_menu.active_buttons()
            return True
        else:
            self.__view_grid_menu.deactivate_buttons()
            return False

    def is_valid_size(self, rows:int, columns:int) -> bool:
        """Vérifie si la taille de grille demandée en entrée est valide.
        Args:
            rows: Nombre de lignes de la grille.
            columns: Nombre de colonnes de la grille.
        Returns:
            Vrai si la taille de grille est correct sinon Faux.
        Notes:
            - taille de grille correct : 1 < rows < 9 et 1 < columns < 9.
        """
        try:
            if (int(rows) > 1 and int(rows) < 9) and (int(columns) > 1 and int(columns) < 9):
                self.__view_grid_menu.deactivate_popup_grid_size()
                self.__game_settings.set_rows(int(rows))
                self.__game_settings.set_columns(int(columns))
                return True
            else:
                self.__view_grid_menu.active_popup_grid_size()
                return False
        except ValueError:
            self.__view_grid_menu.active_popup_grid_size()
            return False

    def is_valid_cards(self, cards:int) -> bool:
        """Vérifie si le nombre de cartes demandée en entrée est valide.
        Args:
            cards: Nombre de cartes dans la grille.
        Returns:
            Vrai si le nombre de cartes est correct sinon Faux.
        Notes:
            - nombre de cartes correct : 6 < cards < 35.
        """
        try:
            if int(cards) > 6 and int(cards) < 35:
                self.__view_grid_menu.deactivate_popup_text_cards()
                self.__game_settings.set_cards(int(cards))
                return True
            else:
                self.__view_grid_menu.active_popup_text_cards()
                return False
        except ValueError:
            self.__view_grid_menu.active_popup_text_cards()
            return False

    def grid_shape(self, shape:str) -> None:
        """Modifie la forme de la grille.
        Args:
            shape: forme de la grille.
        Notes:
            - Modifie la forme de la grille.
            - Utile pour le menu de paramétrage de la grille.
            - désactive les buttons pour choisir la taille/nombre de cartes de la grille si shape != "classic" sinon active les buttons.
        """
        self.__game_settings.set_shape(shape)
        self.__view_grid_menu.active_buttons() if shape == "classic" else self.__view_grid_menu.deactivate_buttons()