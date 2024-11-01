# -*- coding: utf-8 -*-

###########################################
#                modules                  #
###########################################
from model.utils.JsonLoader import JsonLoader
from model.ObservableModel import ObservableModel
###########################################

class GameSettings(ObservableModel):
    """Représente un modèle contenant un dictionnaire de paramètres (couleur, taille de la grille, etc...) pour le jeu.
    Args:
        json_loader: classe représentant le chargement des données d'un fichier JSON.
    Notes:
        - La classe hérite de ObservableModel.
    """

    def __init__(self):
        super().__init__()
        self.__json_loader = JsonLoader("./config/settings.json")

    def get_color_theme(self) -> str:
        return self.__json_loader.get_setting("color_settings", "color_theme")

    def get_color_button_background(self) -> str:
        return self.__json_loader.get_setting("color_settings", "color_button_background")

    def get_color_button_foreground(self) -> str:
        return self.__json_loader.get_setting("color_settings", "color_button_foreground")

    def get_color_button_activebackground(self) -> str:
        return self.__json_loader.get_setting("color_settings", "color_button_activebackground")

    def get_color_button_activeforeground(self) -> str:
        return self.__json_loader.get_setting("color_settings", "color_button_activeforeground")

    def get_shape(self) -> str:
        return self.__json_loader.get_setting("grid_settings", "shape")

    def set_color_theme(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_theme", color)
        self._notify_theme_change(color)

    def set_color_button_background(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_button_background", color)
        self._notify_theme_change(color)

    def set_color_button_foreground(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_button_foreground", color)
        self._notify_theme_change(color)

    def set_color_button_activebackground(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_button_activebackground", color)
        self._notify_theme_change(color)

    def set_color_button_activeforeground(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_button_activeforeground", color)
        self._notify_theme_change(color)

    def set_color_canvas_grid(self, color:str) -> None:
        self.__json_loader.modify_settings("color_settings", "color_canvas_grid", color)
        self._notify_theme_change(color)

    def set_rows(self, rows:int) -> None:
        self.__json_loader.modify_settings("grid_settings", "rows", rows)

    def set_columns(self, columns:int) -> None:
        self.__json_loader.modify_settings("grid_settings", "columns", columns)

    def set_cards(self, cards:int) -> None:
        self.__json_loader.modify_settings("grid_settings", "cards", cards)

    def set_shape(self, shape:str) -> None:
        self.__json_loader.modify_settings("grid_settings", "shape", shape)

    def forced_loading(self) -> None:
        """Forcer le modèle à prévenir ses observeurs/écouteurs.
        Notes:
            - Utilisé uniquement lors du chargement du jeu.
            - Permet de mettre à jour les couleurs du jeu.
        """
        self._notify_colors_change(self.get_color_theme(),
                                    self.get_color_button_background(),
                                    self.get_color_button_foreground(),
                                    self.get_color_button_activebackground(),
                                    self.get_color_button_activeforeground())
        