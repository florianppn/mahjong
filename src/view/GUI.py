# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.Mahjong import Mahjong
from view import *
from controller import *
###########################################

class GUI(Tk):
    """Représente l'interface graphique de l'utilisateur."""

    def __init__(self, mahjong:Mahjong):
        super().__init__()
        self.title("Mahjong")
        self.__mahjong = mahjong
        self.config(bg='#557788')

        self.__grid_view = GridView(self, self.__mahjong)
        self.__grid_view.grid(row=1, column=0, columnspan=10)
        self.__end_view = Canvas(self, width=650, height=800, bg='#557788', highlightthickness=2, highlightbackground="black")
        self.__end_view.grid_forget()

        mouse_controller = MouseController(self, self.__mahjong, self.__grid_view)
        self.bind('<Button-1>', mouse_controller.mouse_clicked)

        menu = Frame(self)
        menu.config(bg="#557788")
        menu.grid(row=0, column=0)
        self.__save_menu = SaveMenuController(menu, self.__mahjong)
        self.__save_menu.grid(row=0, column=0)
        OptionsMenuController(self, menu, self.__mahjong).grid(row=0, column=1)
        self.__help_menu = HelpMenuController(menu, self.__mahjong, self.__grid_view)
        self.__help_menu.grid(row=0, column=2)
        StatisticView(menu, self.__mahjong).grid(row=0, column=3, padx=40)

    def show(self, state:int):
        """Montrer la grille de jeu.
        Notes:
            0 - affiche la grille.
            1 - affiche la fin gagnante.
            2 - affiche la fin perdante.
        """
        if state == 0:
            self.__save_menu.config(state="normal")
            self.__help_menu.config(state="normal")
            self.__end_view.grid_forget()
            self.__grid_view.grid(row=1, column=0, columnspan=10)
        elif state == 1:
            self.__save_menu.config(state="disabled")
            self.__help_menu.config(state="disabled")
            self.__grid_view.grid_forget()
            self.__end_view.grid(row=1, column=0, columnspan=10)
            self.__end_view.delete(ALL)
            self.__end_view.create_text(325, 400, text="Bravo, vous avez gagné !", font=("Arial", 20), fill="darkorange")
        elif state == 2:
            self.__save_menu.config(state="disabled")
            self.__help_menu.config(state="disabled")
            self.__grid_view.grid_forget()
            self.__end_view.grid(row=1, column=0, columnspan=10)
            self.__end_view.delete(ALL)
            self.__end_view.create_text(325, 400, text="Dommage, vous avez perdu !", font=("Arial", 20), fill="darkorange")
            
