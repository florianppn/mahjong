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

    def __init__(self, mahjong:Mahjong):
        super().__init__()
        self.title("Mahjong")
        self.__mahjong = mahjong
        self.show_game()
        self.config(bg='#557788')

    def show_game(self):
        mouse_controller = MouseController(self.__mahjong)
        self.bind('<Button-1>', mouse_controller.mouse_clicked)

        grid_view = GridView(self, self.__mahjong)
        grid_view.grid(row=1, column=0, columnspan=10)

        menu = Frame(self)
        menu.config(bg="#557788")
        menu.grid(row=0, column=0)
        SaveMenuController(menu, self.__mahjong).grid(row=0, column=0)
        OptionsMenuController(menu, self.__mahjong).grid(row=0, column=1)
        HelpMenuController(menu, self.__mahjong, grid_view).grid(row=0, column=2)
        StatisticView(menu, self.__mahjong).grid(row=0, column=3, padx=30)

    def show_end(self):
        pass
